const BASE = import.meta.env.VITE_API_URL || "";

function getToken() {
  return localStorage.getItem("kazi_access");
}

function setTokens(access, refresh) {
  localStorage.setItem("kazi_access", access);
  localStorage.setItem("kazi_refresh", refresh);
}

function clearTokens() {
  localStorage.removeItem("kazi_access");
  localStorage.removeItem("kazi_refresh");
  localStorage.removeItem("kazi_user");
}

async function request(method, path, body) {
  const token = getToken();
  const headers = { "Content-Type": "application/json" };
  if (token) headers["Authorization"] = `Bearer ${token}`;

  const res = await fetch(`${BASE}${path}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : undefined,
  });

  let data;
  try {
    data = await res.json();
  } catch {
    data = {};
  }

  if (!res.ok) {
    const message =
      data?.detail ||
      data?.non_field_errors?.[0] ||
      Object.values(data)?.[0]?.[0] ||
      Object.values(data)?.[0] ||
      "Something went wrong";
    throw new Error(typeof message === "string" ? message : JSON.stringify(message));
  }

  return data;
}

export const auth = {
  register: (data) => request("POST", "/api/auth/register/", data),
  login: (data) => request("POST", "/api/auth/login/", data),
  logout: () => request("POST", "/api/auth/logout/"),
};

export const jobs = {
  list: () => request("GET", "/api/client/jobs/"),
  create: (data) => request("POST", "/api/client/jobs/", data),
  acceptBid: (jobId, bidId) =>
    request("POST", `/api/client/jobs/${jobId}/accept-bid/`, { bid_id: bidId }),
};

export const worker = {
  browseJobs: () => request("GET", "/api/worker/browse-jobs/"),
  myBids: () => request("GET", "/api/worker/my-bids/"),
  placeBid: (data) => request("POST", "/api/worker/my-bids/", data),
  markComplete: (bidId) =>
    request("POST", `/api/worker/my-bids/${bidId}/mark-complete/`),
  profile: () => request("GET", "/api/worker/profile/"),
};

export const escrow = {
  list: () => request("GET", "/api/escrow/transactions/"),
  release: (id) =>
    request("POST", `/api/escrow/transactions/${id}/release-funds/`),
  dispute: (id, reason) =>
    request("POST", `/api/escrow/transactions/${id}/raise-dispute/`, { reason }),
};

export const wallet = {
  get: () => request("GET", "/api/wallet/wallet/"),
  withdraw: (amount) =>
    request("POST", "/api/wallet/wallet/withdraw/", { amount }),
};

export const notifications = {
  list: () => request("GET", "/api/notifications/"),
  markRead: (id) => request("POST", `/api/notifications/${id}/mark_as_read/`),
};

export { setTokens, clearTokens };
