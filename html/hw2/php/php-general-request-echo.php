<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=UTF-8");
$method = $_SERVER['REQUEST_METHOD'] ?? 'UNKNOWN';
$headers = function_exists('getallheaders') ? getallheaders() : [];
$raw = file_get_contents('php://input');
?><!doctype html><html><head><title>General Request Echo (PHP)</title></head><body>
<h1>General Request Echo</h1><hr/>
<p>Method: <b><?= htmlspecialchars($method) ?></b></p>
<h3>Headers</h3><pre><?php ksort($headers); print_r($headers); ?></pre>
<h3>Body</h3><pre><?= htmlspecialchars($raw) ?></pre>
</body></html>
