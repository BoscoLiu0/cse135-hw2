<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=UTF-8");
$ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$now = date('r');
?><!doctype html><html><head><title>Hello, PHP!</title></head><body>
<h1>Hello, PHP (HTML)</h1><hr/>
<p>Generated at: <?= htmlspecialchars($now) ?></p>
<p>Your IP: <?= htmlspecialchars($ip) ?></p>
</body></html>
