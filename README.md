# discord-twitter
DiscordのBOTを常駐させたチャンネルでのチャット及びBOT宛のメッセージを受信すると指定したTwitterアカウントにユーザー名とチャット内容をDMで送信する<br>
(Herokuで動作中)

- DiscordDeveloperPortal (https://discordapp.com/developers) でDiscordBotを作成
- TwitterDeveloperPlatform (https://developer.twitter.com/content/developer-twitter/ja.html) で開発者登録を行い各種Keyを取得
- DM送信を行う対象のTwtter.user_idを確認
- チャットを受信したいサーバにDiscordBotを設置

.env.sumpleは.envのサンプルファイルです。上記箇所で取得した値を設定して使用してください。
