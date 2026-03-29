// LOAD DATA
let jobs = JSON.parse(localStorage.getItem("jobs")) || [];
let products = [
  { name: "Shoes", price: 3000 },
  { name: "Sofa", price: 15000 },
];

// POST JOB
const form = document.getElementById("jobForm");
if (form) {
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const job = {
      title: document.getElementById("title").value,
      desc: document.getElementById("desc").value,
      price: document.getElementById("price").value,
    };

    jobs.push(job);
    localStorage.setItem("jobs", JSON.stringify(jobs));

    alert("Job posted!");
    form.reset();
  });
}

// DISPLAY JOBS
const jobListEl = document.getElementById("jobList");
if (jobListEl) {
  jobListEl.innerHTML = jobs.length
    ? jobs
        .map(
          (job, i) => `
        <div class="card">
          <h3>${job.title}</h3>
          <p>${job.desc}</p>
          <p>Ksh ${job.price}</p>
          <a href="job-details.html" onclick="selectJob(${i})">View</a>
        </div>
      `,
        )
        .join("")
    : "<p>No jobs yet</p>";
}

// DISPLAY PRODUCTS
const productListEl =
  document.getElementById("productList") ||
  document.getElementById("marketList");
if (productListEl) {
  productListEl.innerHTML = products
    .map(
      (p, i) => `
    <div class="card">
      <h3>${p.name}</h3>
      <p>Ksh ${p.price}</p>
      <a href="product-details.html" onclick="selectProduct(${i})">View</a>
    </div>
  `,
    )
    .join("");
}

// PAYMENT
function payNow() {
  const status = document.getElementById("status");
  if (!status) return;

  status.innerText = "Payment Held Securely...";

  setTimeout(() => {
    status.innerText = "Waiting for delivery confirmation...";
  }, 1500);
}

// CONFIRM DELIVERY (ESCROW RELEASE)
function confirmDelivery() {
  alert("Delivery confirmed. Funds released ✅");
}

// DASHBOARD

// ── Default seed data ──────────────────────────────────────────────
const DEFAULT_JOBS = [
  {
    id: "j1",
    title: "Website Redesign — Nairobi Bakery",
    description:
      "Full redesign of a local bakery site: new branding, mobile responsive, online ordering.",
    price: 45000,
    status: "In Progress",
  },
  {
    id: "j2",
    title: "Logo Design for Tech Startup",
    description:
      "Modern logo + brand identity kit. Three rounds of revisions included.",
    price: 12000,
    status: "Pending",
  },
  {
    id: "j3",
    title: "Copywriting — 10 Blog Articles",
    description:
      "SEO-optimised long-form articles for a fintech blog, 1 500 words each.",
    price: 30000,
    status: "Completed",
  },
];

const DEFAULT_ORDERS = [
  {
    id: "o1",
    name: "Professional Camera Lens 50mm f/1.8",
    description:
      "Canon EF 50mm f/1.8 STM — brand new, boxed, warranty included.",
    price: 18500,
    status: "Pending",
  },
  {
    id: "o2",
    name: "Ergonomic Office Chair",
    description:
      "Lumbar support, adjustable armrests, breathable mesh back — Nairobi delivery.",
    price: 24000,
    status: "Delivered",
  },
];

const DEFAULT_PAYMENTS = [
  {
    ref: "KE-2024-001",
    desc: "Website Redesign — Nairobi Bakery",
    amount: 45000,
    status: "Held",
    date: "12 Jun 2025",
  },
  {
    ref: "KE-2024-002",
    desc: "Logo Design for Tech Startup",
    amount: 12000,
    status: "Awaiting",
    date: "18 Jun 2025",
  },
  {
    ref: "KE-2024-003",
    desc: "Blog Copywriting x10",
    amount: 30000,
    status: "Released",
    date: "5 Jun 2025",
  },
  {
    ref: "KE-2024-004",
    desc: "Camera Lens Purchase",
    amount: 18500,
    status: "Held",
    date: "20 Jun 2025",
  },
  {
    ref: "KE-2024-005",
    desc: "Office Chair Purchase",
    amount: 24000,
    status: "Released",
    date: "1 Jun 2025",
  },
];

// ── Storage helpers ────────────────────────────────────────────────
function load(key, def) {
  try {
    return JSON.parse(localStorage.getItem(key)) || def;
  } catch {
    return def;
  }
}
function save(key, val) {
  localStorage.setItem(key, JSON.stringify(val));
}

function seed() {
  if (!localStorage.getItem("kazi_jobs")) save("kazi_jobs", DEFAULT_JOBS);
  if (!localStorage.getItem("kazi_orders")) save("kazi_orders", DEFAULT_ORDERS);
  if (!localStorage.getItem("kazi_payments"))
    save("kazi_payments", DEFAULT_PAYMENTS);
}

// ── Toast ──────────────────────────────────────────────────────────
let toastTimer;
function showToast(msg) {
  const t = document.getElementById("toast");
  document.getElementById("toast-msg").textContent = msg;
  t.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove("show"), 3200);
}

// ── Format currency ────────────────────────────────────────────────
const fmt = (n) => "KES " + Number(n).toLocaleString("en-KE");

// ── Badge HTML ─────────────────────────────────────────────────────
function badge(status) {
  const map = {
    Pending: "pending",
    "In Progress": "in-progress",
    Completed: "completed",
    Delivered: "delivered",
    Held: "held",
    Awaiting: "awaiting",
    Released: "released",
  };
  const cls = map[status] || "pending";
  return `<span class="badge ${cls}">${status}</span>`;
}

// ── Render Jobs ────────────────────────────────────────────────────
function renderJobs() {
  const jobs = load("kazi_jobs", DEFAULT_JOBS);
  const container = document.getElementById("jobs-container");
  document.getElementById("jobs-count").textContent = jobs.length;

  if (!jobs.length) {
    container.innerHTML = `<div class="empty-state"><div class="icon">📋</div><p>No jobs yet.</p></div>`;
    return;
  }

  container.innerHTML = jobs
    .map((job) => {
      const accentCls =
        {
          Pending: "pending",
          "In Progress": "progress",
          Completed: "completed",
        }[job.status] || "pending";
      const canConfirm = job.status === "Completed";
      const btnLabel =
        job.status === "Completed"
          ? "✓ Confirm Completion"
          : job.status === "In Progress"
            ? "⏳ In Progress"
            : "🕐 Awaiting Start";

      return `
    <div class="card" id="job-${job.id}">
      <div class="card-accent ${accentCls}"></div>
      <div class="card-body">
        <div class="card-title">${job.title}</div>
        <div class="card-desc">${job.description}</div>
        <div class="card-meta">
          <div class="price">${fmt(job.price)} <span>KES</span></div>
          ${badge(job.status)}
        </div>
      </div>
      <div class="card-footer">
        <button
          class="btn btn-primary btn-full btn-sm"
          ${canConfirm ? "" : "disabled"}
          onclick="confirmJob('${job.id}')"
        >${btnLabel}</button>
      </div>
    </div>`;
    })
    .join("");
}

function confirmJob(id) {
  const jobs = load("kazi_jobs", DEFAULT_JOBS);
  const job = jobs.find((j) => j.id === id);
  if (!job || job.status !== "Completed") return;

  // Release escrow payment
  const payments = load("kazi_payments", DEFAULT_PAYMENTS);
  const pay = payments.find((p) =>
    p.desc.toLowerCase().includes(job.title.toLowerCase().slice(0, 15)),
  );
  if (pay && pay.status !== "Released") pay.status = "Released";
  save("kazi_payments", payments);

  showToast(`Job "${job.title}" confirmed. Escrow released! 🎉`);
  renderAll();
}

// ── Render Orders ──────────────────────────────────────────────────
function renderOrders() {
  const orders = load("kazi_orders", DEFAULT_ORDERS);
  const container = document.getElementById("orders-container");
  document.getElementById("orders-count").textContent = orders.length;

  if (!orders.length) {
    container.innerHTML = `<div class="empty-state"><div class="icon">🛒</div><p>No orders placed yet.</p></div>`;
    return;
  }

  container.innerHTML = orders
    .map((order) => {
      const accentCls = order.status === "Delivered" ? "delivered" : "pending";
      const canConfirm = order.status === "Delivered";
      const btnLabel = canConfirm
        ? "✓ Confirm Delivery"
        : "🚚 Awaiting Delivery";

      return `
    <div class="card" id="order-${order.id}">
      <div class="card-accent ${accentCls}"></div>
      <div class="card-body">
        <div class="card-title">${order.name}</div>
        <div class="card-desc">${order.description}</div>
        <div class="card-meta">
          <div class="price">${fmt(order.price)} <span>KES</span></div>
          ${badge(order.status)}
        </div>
      </div>
      <div class="card-footer">
        <button
          class="btn btn-primary btn-full btn-sm"
          ${canConfirm ? "" : "disabled"}
          onclick="confirmDelivery('${order.id}')"
        >${btnLabel}</button>
      </div>
    </div>`;
    })
    .join("");
}

function confirmDelivery(id) {
  const orders = load("kazi_orders", DEFAULT_ORDERS);
  const order = orders.find((o) => o.id === id);
  if (!order || order.status !== "Delivered") return;

  // Update payment to Released
  const payments = load("kazi_payments", DEFAULT_PAYMENTS);
  const pay = payments.find(
    (p) =>
      p.ref === "KE-2024-004" ||
      p.desc.toLowerCase().includes(order.name.toLowerCase().slice(0, 12)),
  );
  if (pay && pay.status !== "Released") pay.status = "Released";
  save("kazi_payments", payments);

  showToast(`Delivery confirmed for "${order.name}". Funds released! 📦`);
  renderAll();
}

// ── Render Payments ────────────────────────────────────────────────
function renderPayments() {
  const payments = load("kazi_payments", DEFAULT_PAYMENTS);
  const tbody = document.getElementById("payments-body");

  let held = 0,
    awaiting = 0,
    released = 0;
  payments.forEach((p) => {
    if (p.status === "Held") held += p.amount;
    if (p.status === "Awaiting") awaiting += 1;
    if (p.status === "Released") released += p.amount;
  });

  document.getElementById("stat-held").textContent = fmt(held);
  document.getElementById("stat-awaiting").textContent = awaiting;
  document.getElementById("stat-released").textContent = fmt(released);

  if (!payments.length) {
    tbody.innerHTML = `<tr><td colspan="5" style="text-align:center;color:var(--grey-400);padding:32px">No records</td></tr>`;
    return;
  }

  tbody.innerHTML = payments
    .map(
      (p) => `
    <tr>
      <td><code style="font-size:12px;background:var(--grey-100);padding:3px 7px;border-radius:4px">${p.ref}</code></td>
      <td>${p.desc}</td>
      <td class="amount-cell">${fmt(p.amount)}</td>
      <td>${badge(p.status)}</td>
      <td style="color:var(--grey-400);font-size:13px">${p.date}</td>
    </tr>
  `,
    )
    .join("");
}

// ── Render all ─────────────────────────────────────────────────────
function renderAll() {
  renderJobs();
  renderOrders();
  renderPayments();
}

// ── Init ───────────────────────────────────────────────────────────
seed();
renderAll();
