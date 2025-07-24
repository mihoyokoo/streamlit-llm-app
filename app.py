from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("この国どんな国？: 世界の国々について知るWebアプリ")

st.write("##### 動作モード1: 国の歴史について知る")
st.write("入力フォームに国名を入力し、「実行」ボタンを押すことでその国の歴史についての情報を取得できます。")
st.write("##### 動作モード2: 国の文化について知る")
st.write("入力フォームに国名を入力し、「実行」ボタンを押すことでその国の文化についての情報を取得できます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["歴史", "文化"]
)

st.divider()

# 入力フォーム
input_message = st.text_input(label="国名を入力してください。", placeholder="例：アメリカ合衆国")

# 実行ボタンが押されたら処理を開始
if st.button("実行"):
    if input_message.strip() == "":
        st.error("国名を入力してから「実行」ボタンを押してください。")
    else:
        st.divider()

        # OpenAI API呼び出し
        from langchain_openai import ChatOpenAI
        from langchain.schema import SystemMessage, HumanMessage

        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

        # モードに応じてメッセージを設定
        if selected_item == "歴史":
            system_prompt = "あなたは世界の歴史に詳しい専門家です。入力された国の歴史に関する情報を提供してください。"
        else:
            system_prompt = "あなたは世界の文化に詳しい専門家です。入力された国の文化に関する情報を提供してください。"

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=input_message),
        ]

        result = llm(messages)

        # 結果を表示
        st.write(result.content)

