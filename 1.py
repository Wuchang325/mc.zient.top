#!/usr/bin/env python3
"""
临时脚本：列出 Ollama 本地模型并快速对话
依赖：requests
pip install requests
"""

import sys
import requests
import json

OLLAMA_HOST = "http://101.33.240.9:11434"  # 默认地址

def list_models():
    """GET /api/tags 获取已下载模型列表"""
    try:
        r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=5)
        r.raise_for_status()
        return [m["name"] for m in r.json().get("models", [])]
    except Exception as e:
        print("❌ 无法连接 Ollama：", e)
        sys.exit(1)

def chat_loop(model):
    """极简对话：每行一问一答，直到用户输入 /bye"""
    print(f"✅ 已选择模型：{model}")
    print("开始聊天！输入 /bye 退出。\n")
    while True:
        try:
            prompt = input("🧑  ").strip()
            if prompt.lower() in {"/bye", "/quit", "/exit"}:
                print("👋 再见！")
                break
            if not prompt:
                continue
            payload = {"model": model, "prompt": prompt, "stream": True}
            r = requests.post(
                f"{OLLAMA_HOST}/api/generate",
                json=payload,
                headers={"Content-Type": "application/json"},
                stream=True,
                timeout=60
            )
            r.raise_for_status()
            print("🤖  ", end="")
            for line in r.iter_lines(delimiter=b"\n"):
                if not line:
                    continue
                chunk = json.loads(line)
                print(chunk.get("response", ""), end="", flush=True)
            print()  # 换行
        except KeyboardInterrupt:
            print("\n👋 再见！")
            break
        except Exception as e:
            print("⚠️  请求出错：", e)

def main():
    models = list_models()
    if not models:
        print("⚠️  本地没有任何模型！先用 ollama pull 拉一个。")
        sys.exit(0)
    print("本地模型列表：")
    for idx, m in enumerate(models, 1):
        print(f"{idx}. {m}")
    try:
        choice = int(input("\n输入序号选择模型：").strip())
        model = models[choice - 1]
    except (ValueError, IndexError):
        print("❌ 输入错误！")
        sys.exit(1)
    chat_loop(model)

if __name__ == "__main__":
    main()