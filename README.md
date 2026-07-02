# Easy-2.0.py: Master Game Editor & Custom Language

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-green.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)

軽量でスタイリッシュなダークモード対応の自作言語インタプリタ ＆ ゲームエディタです。
簡単な日本語または英語のコマンドを入力するだけで、HPゲージの操作、スコア計算、会話イベント、さらには簡易AI応答やランダム要素を取り入れたゲーム的な演出を手軽に構築・実行できます。

A lightweight, dark-mode custom language interpreter and game editor. Write simple commands in Japanese or English to control HP bars, scores, dialogues, countdowns, and even interactive AI responses!

---

## 📸 スクリーンショット / Features
*   **ダークモード UI**: 目に優しいモダンな黒基調のデザイン。
*   **ゲーム UI 連動**: コードから直接HPゲージやSCORE表示をリアルタイム更新。
*   **AI自動応答**: コマンドラインから簡易AIとの対話が可能。
*   **イベント演出**: タイピングアニメーション付きのチャット、バイブレーション（画面フラッシュ）、カウントダウン、BGM再生機能。

---

## 🛠️ 追加された新機能 (New Commands)
従来のバージョンから以下の強力なコマンドが追加されました：
*   `AI [テキスト]` / `ai [text]`: 入力された言葉（「こんにちは」や「勝てる？」など）に応じてAIが自動返答。それ以外は、適当に返答します！🙏
*   `チャット [名前] [セリフ]` / `chat [name] [text]`: ゲームの会話イベント風のタイピング演出。
*   `ランダム [変数名] [最小] [最大]` / `random [var] [min] [max]`: ダイスやガチャ、ランダムダメージに使える数値生成。
*   `カウントダウン [秒数]` / `countdown [sec]`: ログ画面でのタイマー演出。

---

## 🚀 使い方 / Usage

### 1. 起動方法 (How to Run)
Python 3がインストールされている環境で、以下のコマンドを実行します。特別な外部ライブラリのインストールは不要です（標準のTkinterを使用）。

bash
python Easy-2.0.py
## License

Copyright (c) 2026 [あなたの名前または組織名]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://apache.org

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
