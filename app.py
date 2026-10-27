from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
  message_sent = False

  if request.method == "POST":
    name = request.form.get("name")
    contact_info = request.form.get("contact_info")
    user_message = request.form.get("message")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # حفظ الرسالة سرياً داخل ملف خاص في مشروعك
    with open("private_messages.txt", "a", encoding="utf-8") as file:
      file.write(
          f"--- رسالة جديدة [{timestamp}] ---\n"
          f"الاسم: {name}\n"
          f"التواصل: {contact_info}\n"
          f"الرسالة: {user_message}\n"
          "-----------------------------------\n\n"
      )

    message_sent = True

  socials = {
      "kick": {"username": "2bo5li", "url": "https://kick.com/2bo5li"},
      "twitter": {"username": "2bo5li", "url": "https://twitter.com/2bo5li"},
      "snapchat": {"username": "a2bo5li", "url": "https://snapchat.com/add/a2bo5li"},
      "tiktok": {"username": "2bo5li", "url": "https://tiktok.com/@2bo5li"},
  }

  stream_schedule = {
      "days": "من الأحد إلى الخميس",
      "time": "العاشرة مساءً بتوقيت مكة المكرمة",
      "status": "يتم الإعلان عن البثوث الخاصة قبلها عبر سناب وتويتر!",
  }

  return render_template(
      "index.html",
      socials=socials,
      schedule=stream_schedule,
      message_sent=message_sent,
  )


if __name__ == "__main__":
  app.run(debug=True)