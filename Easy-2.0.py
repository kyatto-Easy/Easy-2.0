import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import time
import random
import string
import os

# メモリと状態の管理
variables = {}
output_widget = None
SAVE_FILE_NAME = "my_code.txt"  # コードを保存するファイル名

# --- 多言語メッセージの設定（サンプルコードを「計算」に修正） ---
LANG_TEXTS = {
    "日本語": {
        "title": "コードエディタ", 
        "label": "", 
        "btn": "▶ 実行する", 
        "output": "ログ:",
        "btn_save": "保存",
        "btn_load": "読込",
        "btn_close": "❌ 終了",
        "sample": "計算 得点 = 0\n得点 得点\n\nチャット ナビゲーター 謎のAIを起動します...\nAI こんにちは\n\n表示 運試しをします！\nランダム 補正値 10 50\n計算 得点 = 得点 + 補正値\n得点 得点\n\nカウントダウン 3\n表示 ゲームクリア！"
    },
    "English": {
        "title": "Code Editor", 
        "label": "", 
        "btn": "▶ RUN", 
        "output": "Log:",
        "btn_save": "Save",
        "btn_load": "Load",
        "btn_close": "❌ CLOSE",
        "sample": "calc score = 0\nscore score\n\nchat Navigator Launching AI...\nai hello\n\nprint Roll the dice!\nrandom bonus 10 50\ncalc score = score + bonus\nscore score\n\ncountdown 3\nprint Game Clear!"
    }
}

# --- 画面（GUI）の構築 ---
root = tk.Tk()
root.title("Code Editor")
root.geometry("420x680")
root.configure(bg="#1e1e1e")
APP_FONT = ("Helvetica", 11)

style = ttk.Style()
style.theme_use("default")
style.configure("TCombobox", fieldbackground="#2d2d2d", background="#1e1e1e", foreground="#ffffff")
style.configure("Horizontal.TProgressbar", background="#4caf50", troughcolor="#2d2d2d")

frame_game_ui = tk.LabelFrame(root, text=" STATUS ", font=("Helvetica", 9, "bold"), fg="#90caf9", bg="#1e1e1e", bd=1)
frame_game_ui.pack(fill="x", padx=10, pady=5)

label_hp_title = tk.Label(frame_game_ui, text="HP:", font=("Helvetica", 10, "bold"), fg="#ffffff", bg="#1e1e1e")
label_hp_title.pack(side="left", padx=(5, 2))

progress_hp = ttk.Progressbar(frame_game_ui, orient="horizontal", length=150, mode="determinate", style="Horizontal.TProgressbar")
progress_hp.pack(side="left", padx=5, pady=5)
progress_hp["value"] = 100

label_score = tk.Label(frame_game_ui, text="SCORE: 0", font=("Helvetica", 11, "bold"), fg="#ffb74d", bg="#1e1e1e")
label_score.pack(side="right", padx=10)


def evaluate_expression(expr):
    expr = expr.strip()
    if expr in variables:
        return variables[expr]
    try:
        if "." in expr:
            return float(expr)
        return int(expr)
    except ValueError:
        return expr

def evaluate_condition(condition_str):
    operators = ["==", "!=", ">=", "<=", ">", "<"]
    for op in operators:
        if op in condition_str:
            left_str, right_str = condition_str.split(op, 1)
            left_val = evaluate_expression(left_str)
            right_val = evaluate_expression(right_str)
            try:
                left_val, right_val = float(left_val), float(right_val)
            except:
                left_val, right_val = str(left_val), str(right_val)
            if op == "==": return left_val == right_val
            if op == "!=": return left_val != right_val
            if op == ">=": return left_val >= right_val
            if op == "<=": return left_val <= right_val
            if op == ">": return left_val > right_val
            if op == "<": return left_val < right_val
    return False

# AI応答（文字化け回避のため絵文字を除去）
def get_ai_response(user_text):
    text = user_text.lower().strip()
    if "こんにちは" in text or "hello" in text:
        return "[AI] こんにちは！私はあなたのゲームのアシスタントです。"
    elif "勝てる" in text or "win" in text:
        return f"[AI] 現在のSCOREは {variables.get('得点', variables.get('score', 0))} ですね。油断しなければ勝てます！"
    elif "疲れた" in text or "tired" in text:
        return "[AI] お疲れ様です。「待つ」コマンドを入れて少し休憩しましょう。"
    elif "ヘルプ" in text or "help" in text:
        return "[AI] HP, 得点, チャット, ランダム, カウントダウン コマンドが使えますよ。"
    else:
        responses = [
            "[AI] フム、奥が深いコードですね。",
            "[AI] その調子でプログラムを動かしましょう！",
            "[AI] 次のコマンドを実行する準備はできています。"
        ]
        return random.choice(responses)

def press_save_file():
    user_code = code_entry.get("1.0", tk.END).strip()
    try:
        with open(SAVE_FILE_NAME, "w", encoding="utf-8") as f:
            f.write(user_code)
        lang = lang_combo.get()
        messagebox.showinfo("成功" if lang == "日本語" else "Success", "Saved!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def press_load_file():
    if not os.path.exists(SAVE_FILE_NAME):
        return
    try:
        with open(SAVE_FILE_NAME, "r", encoding="utf-8") as f:
            content = f.read()
        code_entry.delete("1.0", tk.END)
        code_entry.insert("1.0", content)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def press_close_app():
    root.destroy()

def on_language_change(event=None):
    lang = lang_combo.get()
    text = LANG_TEXTS[lang]
    root.title(text["title"])
    label_code.config(text=text["label"])
    btn_run.config(text=text["btn"])
    label_out.config(text=text["output"])
    btn_save_file.config(text=text["btn_save"])
    btn_load_file.config(text=text["btn_load"])
    btn_close.config(text=text["btn_close"])
    code_entry.delete("1.0", tk.END)
    code_entry.insert("1.0", text["sample"])

frame_top = tk.Frame(root, bg="#1e1e1e")
frame_top.pack(fill="x", padx=10, pady=5)

lang_combo = ttk.Combobox(frame_top, values=list(LANG_TEXTS.keys()), state="readonly", width=8, font=APP_FONT)
lang_combo.set("日本語")
lang_combo.pack(side="left")
lang_combo.bind("<<ComboboxSelected>>", on_language_change)

btn_save_file = tk.Button(frame_top, text="", font=("Helvetica", 9), bg="#37474f", fg="#ffffff", activebackground="#455a64", activeforeground="#ffffff", bd=0, padx=8, pady=2, command=press_save_file)
btn_save_file.pack(side="left", padx=5)

btn_load_file = tk.Button(frame_top, text="", font=("Helvetica", 9), bg="#3e2723", fg="#ffffff", activebackground="#4e342e", activeforeground="#ffffff", bd=0, padx=8, pady=2, command=press_load_file)
btn_load_file.pack(side="left", padx=5)

label_code = tk.Label(root, text="", anchor="w", font=APP_FONT, bg="#1e1e1e", fg="#ffffff")
label_code.pack(fill="x", padx=10, pady=(0, 2))

code_entry = tk.Text(root, height=12, font=APP_FONT, bg="#2d2d2d", fg="#ffffff", insertbackground="#ffffff", bd=1, relief="solid")
code_entry.pack(fill="both", expand=True, padx=10, pady=2)


def run_my_language(code):
    global variables
    lines = code.split("\n")
    outputs = []
    if_stack = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("もし ") or line.startswith("if "):
            _, cond_str = line.split(" ", 1)
            is_true = evaluate_condition(cond_str)
            parent_executing = if_stack[-1]["executing"] if if_stack else True
            current_exec = parent_executing and is_true
            if_stack.append({"executing": current_exec, "done": current_exec})
            continue

        if line.startswith("それとも ") or line.startswith("elif "):
            _, cond_str = line.split(" ", 1)
            if if_stack:
                parent_executing = if_stack[:-1][-1]["executing"] if len(if_stack) > 1 else True
                if parent_executing and not if_stack[-1]["done"]:
                    is_true = evaluate_condition(cond_str)
                    if_stack[-1]["executing"] = is_true
                    if is_true: if_stack[-1]["done"] = True
                else:
                    if_stack[-1]["executing"] = False
            continue

        if line in ["その他", "else"]:
            if if_stack:
                parent_executing = if_stack[:-1][-1]["executing"] if len(if_stack) > 1 else True
                if parent_executing and not if_stack[-1]["done"]:
                    if_stack[-1]["executing"] = True
                    if_stack[-1]["done"] = True
                else:
                    if_stack[-1]["executing"] = False
            continue

        if line in ["終わり", "endif"]:
            if if_stack: if_stack.pop()
            continue

        if if_stack and not if_stack[-1]["executing"]:
            continue

        # AIコマンド（文字化け対策済み）
        if any(line.startswith(cmd + " ") for cmd in ["AI", "ai"]):
            _, ai_msg = line.split(" ", 1)
            evaluated_msg = str(evaluate_expression(ai_msg.strip()))
            response = get_ai_response(evaluated_msg)
            outputs.append(f"__TYPE_EFFECT__:{response}")
            continue

        # チャットコマンド（文字化け対策済み）
        if any(line.startswith(cmd + " ") for cmd in ["チャット", "chat"]):
            _, rest = line.split(" ", 1)
            parts = rest.strip().split(" ", 1)
            if len(parts) == 2:
                speaker, dialogue = parts
                dialogue_val = str(evaluate_expression(dialogue.strip()))
                outputs.append(f"__TYPE_EFFECT__:[{speaker}]: {dialogue_val}")
            continue

        if any(line.startswith(cmd + " ") for cmd in ["ランダム", "random"]):
            _, rest = line.split(" ", 1)
            parts = rest.strip().split()
            if len(parts) == 3:
                var_name, min_str, max_str = parts
                v_min = int(evaluate_expression(min_str))
                v_max = int(evaluate_expression(max_str))
                rand_res = random.randint(v_min, v_max)
                variables[var_name.strip()] = rand_res
                outputs.append(f"[RANDOM] {var_name.strip()} = {rand_res}")
            continue

        # カウントダウン（文字化け対策済み）
        if any(line.startswith(cmd + " ") for cmd in ["カウントダウン", "countdown"]):
            _, sec_str = line.split(" ", 1)
            seconds = int(evaluate_expression(sec_str.strip()))
            for i in range(seconds, 0, -1):
                outputs.append(f"■ {i}...")
            continue

        if any(line.startswith(cmd + " ") for cmd in ["HP", "hp"]):
            _, val_str = line.split(" ", 1)
            hp_val = int(evaluate_expression(val_str.strip()))
            hp_val = max(0, min(100, hp_val))
            progress_hp["value"] = hp_val
            root.update()
            outputs.append(f"[GAME UI] HP updated to {hp_val}%")
            continue

        if any(line.startswith(cmd + " ") for cmd in ["得点", "score"]):
            _, val_str = line.split(" ", 1)
            score_val = evaluate_expression(val_str.strip())
            label_score.config(text=f"SCORE: {score_val}")
            root.update()
            outputs.append(f"[GAME UI] Score updated to {score_val}")
            continue

        if any(line.startswith(cmd + " ") for cmd in ["音楽", "bgm"]):
            _, file_str = line.split(" ", 1)
            filename = str(evaluate_expression(file_str.strip()))
            outputs.append(f"[BGM] Play request: {filename}")
            if os.name == "nt":
                import winsound
                try:
                    winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
                except:
                    outputs.append(f"[BGM_ERROR] Could not play {filename}")
            else:
                outputs.append("[BGM] OS standard sound play triggered")
            continue

        if line in ["音楽停止", "bgm_stop"]:
            if os.name == "nt":
                import winsound
                winsound.PlaySound(None, winsound.SND_PURGE)
            outputs.append("[BGM] Stopped all music")
            continue

        if any(line.startswith(cmd + " ") for cmd in ["計算", "calc"]):
            _, rest = line.split(" ", 1)
            var_name, expr_str = rest.split("=", 1)
            parsed_expr = expr_str.strip()
            for v_name, v_val in variables.items():
                parsed_expr = parsed_expr.replace(v_name, str(v_val))
            try:
                if all(c in "0123456789+-*/(). " for c in parsed_expr):
                    calc_res = eval(parsed_expr)
                    variables[var_name.strip()] = calc_res
                    outputs.append(f"[CALC] {var_name.strip()} = {calc_res}")
            except:
                outputs.append("[CALC_ERROR] Failed")
            continue

        if any(line.startswith(cmd + " ") for cmd in ["カラー", "color"]):
            _, color_name = line.split(" ", 1)
            outputs.append(f"[COLOR] Background -> {color_name.strip()}")
            continue

        if any(line.startswith(cmd + " ") for cmd in ["バイブ", "vibe"]):
            _, count_str = line.split(" ", 1)
            count = int(evaluate_expression(count_str.strip()))
            orig_bg = output_widget.cget("bg")
            for _ in range(min(count, 10)):
                output_widget.config(bg="#d32f2f"); root.update(); time.sleep(0.06)
                output_widget.config(bg=orig_bg); root.update(); time.sleep(0.06)
            outputs.append(f"[VIBE] Shook {count} times")
            continue

        if line in ["消去", "clear"]: outputs = ["CLEAR_SIGNAL"]; continue
        if line in ["音", "beep"]: root.bell(); outputs.append("[BEEP]"); continue
        if line in ["アプリ終了", "close"]: root.destroy(); return "CLOSED"
        
        if any(line.startswith(cmd + " ") for cmd in ["警告", "alert"]):
            _, msg = line.split(" ", 1)
            msg_val = str(evaluate_expression(msg.strip()))
            messagebox.showwarning("Alert", msg_val)
            continue
        if any(line.startswith(cmd + " ") for cmd in ["アニメ", "type"]):
            _, msg = line.split(" ", 1)
            outputs.append(f"__TYPE_EFFECT__:{str(evaluate_expression(msg.strip()))}")
            continue
        if any(line.startswith(cmd + " ") for cmd in ["待つ", "wait"]):
            _, sec_str = line.split(" ", 1)
            time.sleep(float(evaluate_expression(sec_str.strip())))
            continue
        if any(line.startswith(cmd + " ") for cmd in ["表示", "print"]):
            _, expr = line.split(" ", 1)
            outputs.append(str(evaluate_expression(expr.strip())))
            continue

    return outputs

def animate_text(target_widget, text_line, delay=0.04):
    for char in text_line:
        target_widget.insert(tk.END, char); target_widget.see(tk.END); target_widget.update(); time.sleep(delay)
    target_widget.insert(tk.END, "\n")

def press_run_code():
    user_code = code_entry.get("1.0", tk.END)
    global variables
    variables = {}
    
    progress_hp["value"] = 100
    label_score.config(text="SCORE: 0")
    
    results = run_my_language(user_code)
    if results == "CLOSED": return
        
    output_widget.config(state="normal")
    output_widget.delete("1.0", tk.END)
    
    for res in results:
        if res.startswith("__TYPE_EFFECT__:"):
            animate_text(output_widget, res.replace("__TYPE_EFFECT__:", ""))
        else:
            output_widget.insert(tk.END, res + "\n")
    output_widget.see(tk.END)
    output_widget.config(state="disabled")

btn_run = tk.Button(root, text="", font=("Helvetica", 12, "bold"), bg="#2e7d32", fg="#ffffff", activebackground="#1b5e20", activeforeground="#ffffff", bd=0, command=press_run_code)
btn_run.pack(fill="x", padx=10, pady=5)

label_out = tk.Label(root, text="", anchor="w", font=APP_FONT, bg="#1e1e1e", fg="#ffffff")
label_out.pack(fill="x", padx=10, pady=(5, 2))

output_widget = tk.Text(root, height=6, font=APP_FONT, bg="#2d2d2d", fg="#eceff1", state="disabled", bd=1, relief="solid")
output_widget.pack(fill="both", expand=True, padx=10, pady=(2, 10))

btn_close = tk.Button(root, text="", font=("Helvetica", 10), bg="#c62828", fg="#ffffff", activebackground="#b71c1c", activeforeground="#ffffff", bd=0, padx=10, command=press_close_app)
btn_close.pack(side="right", padx=10, pady=(0, 10))

on_language_change()
root.mainloop()
