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
*   `AI [テキスト]` / `ai [text]`: 入力された言葉（「こんにちは」や「勝てる？」など）に応じてAIが自動返答。
*   `チャット [名前] [セリフ]` / `chat [name] [text]`: ゲームの会話イベント風のタイピング演出。
*   `ランダム [変数名] [最小] [最大]` / `random [var] [min] [max]`: ダイスやガチャ、ランダムダメージに使える数値生成。
*   `カウントダウン [秒数]` / `countdown [sec]`: ログ画面でのタイマー演出。

---

## 🚀 使い方 / Usage

### 1. 起動方法 (How to Run)
Python 3がインストールされている環境で、以下のコマンドを実行します。特別な外部ライブラリのインストールは不要です（標準のTkinterを使用）。

```bash
python Easy-2.0.py
## ⚠️ ライセンスと著作権について / License and Copyright

このプロジェクトは **GNU General Public License v3.0 (GPLv3)** のもとで公開されています。

- **無断転載・パクリの禁止**: 本プロジェクトのコードをコピー・改変して、自身の成果物として隠蔽・独占配布することはライセンス違反です。
- **ソースコード公開の義務**: 本プロジェクトのコードを一部でも使用または改変して再配布する場合、**その成果物のソースコードも完全にGPLv3で公開する義務**が発生します。
- **著作権表示の義務**: コードを利用・改変する際は、必ず原作者（minaton）の著作権表示を残す必要があります。

悪質な無断転載やライセンス違反を発見した場合は、GitHubへのDMCAテイクダウン申請（強制削除申し立て）を含めた法的措置を即座に講じます。

---

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.

- **Copyleft**: Any derivative work or modifications of this source code **must also be open-sourced under the GPLv3**.
- **Attribution**: You must retain the original copyright notice and give appropriate credit to the author.
- Unauthorized copying, distribution, or plagiarism without complying with the GPLv3 terms will result in an immediate **DMCA takedown notice** to GitHub.

Copyright (c) 2026 minaton

