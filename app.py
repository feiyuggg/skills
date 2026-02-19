from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

participants = []
prizes = []
winners = []

HTML = """
<!doctype html>
<html lang=\"zh\">
<head>
  <meta charset=\"UTF-8\">
  <title>抽奖系统</title>
  <style>
    body { font-family: Arial; max-width: 800px; margin: 30px auto; }
    h2 { margin-top: 28px; }
    input, button { padding: 8px; margin: 4px; }
    .card { border: 1px solid #ddd; border-radius: 8px; padding: 14px; margin: 10px 0; }
    ul { line-height: 1.8; }
  </style>
</head>
<body>
  <h1>🎉 抽奖系统</h1>

  <div class=\"card\">
    <h2>添加参与者</h2>
    <input id=\"participant\" placeholder=\"输入名字\">
    <button onclick=\"addParticipant()\">添加</button>
    <p id=\"pmsg\"></p>
  </div>

  <div class=\"card\">
    <h2>添加奖品</h2>
    <input id=\"prize\" placeholder=\"奖品名\">
    <input id=\"count\" type=\"number\" placeholder=\"数量\" min=\"1\">
    <button onclick=\"addPrize()\">添加</button>
    <p id=\"prmsg\"></p>
  </div>

  <div class=\"card\">
    <h2>抽奖</h2>
    <button onclick=\"draw()\">开始抽奖</button>
    <p id=\"dmsg\"></p>
  </div>

  <div class=\"card\">
    <h2>当前数据</h2>
    <button onclick=\"refresh()\">刷新</button>
    <div id=\"data\"></div>
  </div>

<script>
async function addParticipant() {
  const name = document.getElementById('participant').value.trim();
  const r = await fetch('/participants', {
    method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({name})
  });
  const d = await r.json();
  document.getElementById('pmsg').innerText = d.message || d.error;
  refresh();
}
async function addPrize() {
  const name = document.getElementById('prize').value.trim();
  const count = parseInt(document.getElementById('count').value);
  const r = await fetch('/prizes', {
    method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({name, count})
  });
  const d = await r.json();
  document.getElementById('prmsg').innerText = d.message || d.error;
  refresh();
}
async function draw() {
  const r = await fetch('/draw', {method:'POST'});
  const d = await r.json();
  document.getElementById('dmsg').innerText = d.message || d.error;
  refresh();
}
async function refresh() {
  const r = await fetch('/state');
  const d = await r.json();
  document.getElementById('data').innerHTML = `
    <p><b>参与者：</b>${d.participants.join('、') || '无'}</p>
    <p><b>奖品：</b>${d.prizes.map(p => `${p.name} x${p.count}`).join('；') || '无'}</p>
    <p><b>中奖记录：</b></p>
    <ul>${d.winners.map(w => `<li>${w.prize} → ${w.winner}</li>`).join('') || '<li>暂无</li>'}</ul>
  `;
}
refresh();
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/participants", methods=["POST"])
def add_participant():
    data = request.get_json() or {}
    name = (data.get("name") or "").strip()
    if not name:
        return jsonify(error="名字不能为空"), 400
    if name in participants:
        return jsonify(error="参与者已存在"), 400
    participants.append(name)
    return jsonify(message=f"已添加参与者：{name}")

@app.route("/prizes", methods=["POST"])
def add_prize():
    data = request.get_json() or {}
    name = (data.get("name") or "").strip()
    count = data.get("count")
    if not name:
        return jsonify(error="奖品名不能为空"), 400
    if not isinstance(count, int) or count <= 0:
        return jsonify(error="数量必须是正整数"), 400
    prizes.append({"name": name, "count": count})
    return jsonify(message=f"已添加奖品：{name} x{count}")

@app.route("/draw", methods=["POST"])
def draw():
    prize = next((p for p in prizes if p["count"] > 0), None)
    if not prize:
        return jsonify(error="没有可抽取的奖品了"), 400

    won_people = {w["winner"] for w in winners}
    candidates = [p for p in participants if p not in won_people]
    if not candidates:
        return jsonify(error="没有可抽奖的候选人（可能都已中奖）"), 400

    winner = random.choice(candidates)
    prize["count"] -= 1
    winners.append({"prize": prize["name"], "winner": winner})
    return jsonify(message=f"🎉 {winner} 抽中了 {prize['name']}")

@app.route("/state")
def state():
    return jsonify(participants=participants, prizes=prizes, winners=winners)

if __name__ == "__main__":
    app.run(debug=False, port=5001)
