# clara-ai.py

import pandas as pd
import time # 匯入 time 模組來計時
import os     # 匯入 os 模組 (用於 system 指令)
import math # 匯入 math 模組用於比較浮點數
import webbrowser # 匯入 webbrowser 模組 (仍用於開啟 URL)
import pathlib    # 匯入 pathlib 模組處理檔案路徑

# --- 學習風格問卷題目 ---
# (保持不變)
QUESTIONNAIRE = [
    {"id": "q1", "text": "問題 1: 當學習一個全新的概念時，您通常覺得哪種方式最容易吸收？", "options": {"1": "觀看包含圖片、圖表或流程圖的說明。", "2": "聽老師、專家講解或與他人討論。", "3": "透過實際操作、模型製作或角色扮演來體驗。"}, "mapping": {"1": "A", "2": "B", "3": "C"}},
    {"id": "q2", "text": "問題 2: 您在回想資訊時，腦中比較容易浮現的是？", "options": {"1": "當時看到的畫面、場景或文字。", "2": "當時聽到的聲音、對話或旋律。", "3": "當時身體的感覺、動作或操作過程。"}, "mapping": {"1": "A", "2": "B", "3": "C"}},
    {"id": "q3", "text": "問題 3: 在學習或吸收新知時，您比較喜歡以下哪種媒體形式？", "options": {"1": "閱讀圖文並茂的書籍、文章或看教學影片。", "2": "聽 Podcast、有聲書或講座錄音。", "3": "使用互動式教學軟體、動手實驗或參加實作工作坊。"}, "mapping": {"1": "A", "2": "B", "3": "C"}},
    {"id": "q4", "text": "問題 4: 當您需要組裝一件物品時，您通常會怎麼做？", "options": {"1": "主要依賴說明書上的圖解或示意圖。", "2": "請別人唸說明書給您聽，或邊聽教學影片邊做。", "3": "先動手摸索零件，邊試邊組裝，參考說明為輔。"}, "mapping": {"1": "A", "2": "B", "3": "C"}},
    {"id": "q5", "text": "問題 5: 理解一個複雜的抽象概念時，哪種方式對您最有幫助？", "options": {"1": "看到將概念視覺化的圖表、心智圖或比喻圖示。", "2": "聽到老師或同學用不同的方式反覆解釋或舉例說明。", "3": "將概念與實際生活經驗連結，或透過具體案例分析來理解。"}, "mapping": {"1": "A", "2": "B", "3": "C"}}
]

# --- 學習風格識別 (互動式問卷) ---
# (此函式保持不變)
def identify_learning_style():
    print("--- 學習風格問卷 ---")
    # ... (程式碼省略，保持不變) ...
    print("請根據您的直覺，輸入最符合您情況的選項數字 (1, 2 或 3)。")
    user_answers = {}
    for question_data in QUESTIONNAIRE:
        print("-" * 20)
        print(question_data["text"])
        for num, option_text in question_data["options"].items(): print(f"  {num}. {option_text}")
        while True:
            user_input = input("您的選擇是 (請輸入 1, 2 或 3): ")
            if user_input in ["1", "2", "3"]:
                user_answers[question_data["id"]] = question_data["mapping"][user_input]
                break
            else: print("輸入無效，請輸入數字 1, 2 或 3。")
    print("\n--- 問卷完成，開始計算風格 ---")
    visual_score, auditory_score, kinesthetic_score = 0, 0, 0
    for i in range(1, 6):
        answer = user_answers.get(f'q{i}')
        if answer == 'A': visual_score += 1
        elif answer == 'B': auditory_score += 1
        elif answer == 'C': kinesthetic_score += 1
    print(f"最終計分結果: 視覺={visual_score}, 聽覺={auditory_score}, 動覺={kinesthetic_score}")
    max_score = max(visual_score, auditory_score, kinesthetic_score)
    if max_score == 0: return "未知"
    if visual_score == max_score: return "視覺型"
    elif auditory_score == max_score: return "聽覺型"
    elif kinesthetic_score == max_score: return "動覺型"
    else: return "未知"

# --- 一元二次方程式小測驗函式 ---
# (此函式保持不變)
def run_quadratic_quiz():
    """
    執行一個簡單的一元二次方程式解根測驗。
    Returns:
        dict: 包含整體表現數據的字典 ('accuracy', 'time_spent', 'confidence', 'total_questions')。
    """
    print("\n--- 一元二次方程式小測驗 ---")
    # ... (程式碼省略，保持不變) ...
    print("請解出下列方程式的實數根。如果只有一個根(重根)，請輸入兩次相同的值。如果無實數根，請輸入 '無解'。")
    quiz_questions = [
        {'equation': 'x² - 5x + 6 = 0', 'roots': {2.0, 3.0}},
        {'equation': 'x² + 4x + 4 = 0', 'roots': {-2.0}},
        {'equation': '2x² - 7x + 3 = 0', 'roots': {0.5, 3.0}},
        {'equation': 'x² - 2x + 5 = 0', 'roots': None}
    ]
    num_correct = 0; total_questions = len(quiz_questions)
    quiz_start_time = time.time()
    for i, q in enumerate(quiz_questions):
        print("-" * 20); print(f"第 {i+1} 題: {q['equation']}")
        user_roots = set(); is_correct = False
        try:
            ans1_str = input("  請輸入第一個根 (若是無解請輸入 '無解'): ")
            if ans1_str.strip().lower() in ['無解', 'none', 'null', 'na']:
                is_correct = (q['roots'] is None)
            else:
                ans2_str = input("  請輸入第二個根 (若是重根請輸入相同數字): ")
                user_r1 = float(ans1_str); user_r2 = float(ans2_str)
                user_roots = {user_r1, user_r2}
                if q['roots'] is not None and len(user_roots) == len(q['roots']):
                    temp_correct_roots = set(q['roots']); match_count = 0
                    for ur in user_roots:
                        for cr in list(temp_correct_roots):
                            if math.isclose(ur, cr, rel_tol=1e-6):
                                temp_correct_roots.remove(cr); match_count += 1; break
                    is_correct = (match_count == len(q['roots']))
                else: is_correct = False
        except ValueError: print("  輸入包含無效數字..."); is_correct = False
        except Exception as e: print(f"  處理答案時發生錯誤: {e}"); is_correct = False
        if is_correct: print("  答對了！"); num_correct += 1
        else: print(f"  答錯了。正確答案是: {q['roots'] if q['roots'] is not None else '無實數根'}")
    quiz_end_time = time.time(); total_time_spent = quiz_end_time - quiz_start_time
    accuracy = num_correct / total_questions
    print("-" * 20); print(f"測驗完成！總共 {total_questions} 題，答對 {num_correct} 題。")
    print(f"正確率: {accuracy:.2f}, 總花費時間: {total_time_spent:.1f} 秒")
    quiz_confidence = 0
    while True:
        confidence_str = input("您對這次測驗的整體表現信心如何？ (請輸入 1 到 5，1=很不確定, 5=非常有信心): ")
        try:
            confidence_int = int(confidence_str)
            if 1 <= confidence_int <= 5: quiz_confidence = confidence_int; break
            else: print("輸入錯誤，請輸入 1 到 5 之間的數字。")
        except ValueError: print("輸入無效，請輸入數字 1 到 5。")
    return {'accuracy': accuracy, 'time_spent': total_time_spent, 'confidence': quiz_confidence, 'total_questions': total_questions, 'num_correct': num_correct}


# --- 規則式的導師回饋函式 ---
# (此函式保持不變)
def provide_rule_based_feedback(learning_style, performance_data):
    """
    根據學習風格和表現數據(含正確率)，提供預設的規則式回饋。
    """
    accuracy = performance_data.get('accuracy', 0.0)
    # ... (程式碼省略，保持不變) ...
    time_spent = performance_data.get('time_spent', 0)
    confidence = performance_data.get('confidence', 0)
    total_questions = performance_data.get('total_questions', 1)
    avg_time_per_q = time_spent / total_questions if total_questions > 0 else 0
    feedback = ""
    if accuracy < 0.4:
        feedback = "這次測驗看起來有些挑戰喔，沒關係！"
        if confidence <= 2: feedback += " 感覺基礎還不太穩固，別灰心，我們一步步來，先把基礎打好最重要！"
        else: feedback += " 雖然有些題目沒答對，但保持信心是好的開始！我們來看看是哪些觀念需要加強。"
        if learning_style == "視覺型": feedback += " 要不要複習一下圖解步驟或公式推導影片？"
        elif learning_style == "動覺型": feedback += " 試著動手多算幾題基礎練習題？"
    elif accuracy < 0.8:
        feedback = "表現不錯，掌握了大部分！"
        if avg_time_per_q > 60 : feedback += " 不過平均解題時間可以再快一點，多練習就會更熟練！"
        if confidence <= 3: feedback += " 對自己可以更有信心一點喔！"
        else: feedback += " 繼續保持！"
    else:
        feedback = "太厲害了！這次測驗表現非常出色！"
        if confidence <= 3: feedback += " 要相信自己的能力，你做得很好！"
        if avg_time_per_q < 30 : feedback += " 解題速度也很快！"
    print("\n--- AI 導師 Clara (規則式回饋) ---")
    print(feedback)
    print("-" * 20)


# --- 修改：開啟資源的函式 (改用 os.system on Windows) ---
def open_resource(resource_path):
    """
    嘗試使用預設應用程式開啟指定的本地檔案或網址。
    (修正版：對本地檔案優先嘗試使用 Windows 的 start 指令)
    """
    try:
        if "://" in resource_path: # 簡單判斷是否為 URL
             print(f"[正在嘗試開啟網頁資源: {resource_path}]")
             webbrowser.open(resource_path) # 開啟 URL 仍可用 webbrowser
             return True
        else: # 假設是本地檔案
            script_dir = pathlib.Path(__file__).parent.resolve()
            filepath = script_dir / resource_path

            if filepath.is_file():
                print(f"[正在嘗試開啟本地檔案: {filepath}]")
                # --- 修改開始 ---
                # 優先嘗試使用 Windows 的 'start' 指令
                # "" 作為標題是 start 指令的一個怪癖，避免路徑有空格時出錯
                try:
                    os.system(f'start "" "{filepath}"')
                    print("[已嘗試使用 'start' 指令開啟]")
                    return True
                except Exception as e_os:
                    print(f"[使用 'start' 指令失敗: {e_os}]")
                    # 如果 'start' 失敗 (例如非 Windows 系統)，退回使用 webbrowser
                    print("[退回嘗試使用 webbrowser 開啟...]")
                    webbrowser.open(filepath.as_uri())
                    return True
                # --- 修改結束 ---
            else:
                print(f"[錯誤] 在腳本目錄下找不到檔案: {filepath}")
                print(f"請確認在與 clara-ai.py 相同的目錄下有名為 '{resource_path}' 的檔案。")
                return False
    except Exception as e:
        print(f"[錯誤] 開啟資源 '{resource_path}' 時發生問題: {e}")
        return False

# --- 教材推薦函式 (加入開啟影音連結) ---
# (此函式保持不變，但會呼叫修改後的 open_resource)
def recommend_quadratic_material(learning_style, performance_data):
    """
    根據學習風格 和 學習表現(正確率) 推薦學習一元二次方程式的材料。
    (修正影音連結，使用更可靠的 URL)
    """
    accuracy = performance_data.get('accuracy', 0.0)
    # ... (程式碼省略，保持不變) ...
    time_spent = performance_data.get('time_spent', 0)
    confidence = performance_data.get('confidence', 0)
    print(f"\n--- 表現分析 ---")
    print(f"學習風格: '{learning_style}', 測驗正確率: {accuracy:.2f}, "
          f"總花費時間: {time_spent:.1f}s, 信心程度: {confidence}/5")
    recommendation = ""
    video_formula_concept = "https://www.junyiacademy.org/video?v=Z0omOUKCXcg"
    video_solving_example = "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-formula-a1/v/using-the-quadratic-formula"
    video_graphing = "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:features-of-quadratic-functions/v/graphing-a-quadratic-function"
    if accuracy < 0.4:
        recommendation = "基礎尚不穩固，建議先複習基本定義、公式解法。"
        if learning_style == "視覺型":
            recommendation += " 可以從觀看基礎教學影片或閱讀圖文說明開始。\n    這裡有一段關於公式解概念的影片，也許有幫助："
            open_resource(video_formula_concept)
            open_resource("quadratic_formula.png")
        elif learning_style == "聽覺型":
             recommendation += " 也可以找找基礎概念的講解錄音或教學影片。\n    試試看這個公式解概念影片："
             open_resource(video_formula_concept)
        elif learning_style == "動覺型":
            recommendation += " 嘗試用簡單的數字帶入公式動手算算看，或跟著教學影片一步步做。"
            open_resource(video_solving_example)
        else:
            recommendation += " 可以從觀看基礎教學影片或閱讀圖文說明開始。"
            open_resource(video_formula_concept)
    elif accuracy < 0.8:
        recommendation = "掌握了基礎，但可以多加練習以提升熟練度和準確率！"
        if learning_style == "視覺型":
            recommendation += " 推薦使用有圖解步驟的練習題，或觀察不同係數如何影響函數圖形。\n    這個影片或許能幫助理解圖形變化："
            open_resource(video_graphing)
            open_resource("parabola_graph.png")
        elif learning_style == "聽覺型":
            recommendation += " 推薦收聽解題技巧的講解，或嘗試將解題步驟說出來。\n    聽聽這個使用公式解題的範例講解："
            open_resource(video_solving_example)
        elif learning_style == "動覺型":
            recommendation += " 推薦使用互動式習題平台進行練習，或嘗試解應用題。"
        else:
            recommendation += " 推薦從不同類型的練習題著手，找出自己的弱點。"
    else:
        recommendation = "表現很棒！可以挑戰更深入的內容了。"
        if learning_style == "視覺型": recommendation += " 推薦研究二次函數圖形的進階性質或挑戰複雜圖形應用題。"
        elif learning_style == "聽覺型": recommendation += " 推薦聽聽關於一元二次方程式在不同領域應用的講座或討論。"
        elif learning_style == "動覺型": recommendation += " 推薦嘗試解決需要建立模型的實際問題。"
        else: recommendation += " 推薦探索一元二次方程式的延伸應用或挑戰難度較高的綜合題。"
    return recommendation

# --- 產生學習報告的函式 (加入鼓勵語句) ---
# (此函式保持不變)
def generate_report(learning_style, performance_data):
    """
    根據學習風格和表現數據，產生簡單的文字學習報告 (含鼓勵語句)。
    """
    accuracy = performance_data.get('accuracy', 0.0)
    # ... (程式碼省略，保持不變) ...
    time_spent = performance_data.get('time_spent', 0)
    confidence = performance_data.get('confidence', 0)
    num_correct = performance_data.get('num_correct', 0)
    total_questions = performance_data.get('total_questions', 1)
    print("\n--- 本次學習報告 ---")
    print(f"學習風格傾向: {learning_style}")
    print("-" * 20)
    print("學習活動: 一元二次方程式小測驗")
    print(f"  - 測驗題數: {total_questions} 題")
    print(f"  - 答對題數: {num_correct} 題")
    print(f"  - 正確率: {accuracy:.0%}")
    print(f"  - 總花費時間: {time_spent:.1f} 秒")
    print(f"  - 信心程度: {confidence} / 5")
    print("-" * 20)
    overall_comment = ""
    if accuracy >= 0.8: overall_comment = f"整體表現優異 ({accuracy:.0%})，掌握度很高！繼續保持這個學習的勢頭，你真棒！"
    elif accuracy >= 0.4: overall_comment = f"表現不錯 ({accuracy:.0%})，大部分概念已掌握。針對錯誤的部分再努力一下，你會更進步的！"
    else: overall_comment = f"這次正確率 ({accuracy:.0%}) 低了一些，表示基礎可能還需加強。別氣餒，找到適合你的學習方法和資源，一步一步來，一定能克服困難！"
    print(f"總結: {overall_comment}")
    print("=" * 40)


# --- 主程式 (改用 start 指令開啟圖片) ---
# (此函式保持不變)
if __name__ == "__main__":
    print("Clara AI 系統啟動 (改用 start 指令開啟圖片)...")
    print("=" * 40)
    print("提醒：系統可能會嘗試開啟圖片檔案或網頁連結。")
    print("=" * 40)
    user_learning_style = identify_learning_style()
    print(f"\n根據您的回答，您的學習風格傾向為: {user_learning_style}")
    print("=" * 40)
    user_performance_data = run_quadratic_quiz()
    provide_rule_based_feedback(user_learning_style, user_performance_data)
    recommendation = recommend_quadratic_material(user_learning_style, user_performance_data)
    print("\n--- 學習建議 ---")
    print(recommendation)
    print("=" * 40)
    generate_report(user_learning_style, user_performance_data)

