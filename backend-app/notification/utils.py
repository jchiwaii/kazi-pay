def send_kazi_sms(to_phone, message):
    try:
        # Use your short code 23440 as the 'from_' address
        response = sms.send(message, [to_phone], sender_id="23440")
        return response
    except Exception as e:
        print(f"SMS Error: {e}")