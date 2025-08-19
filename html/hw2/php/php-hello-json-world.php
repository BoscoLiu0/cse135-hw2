<?php
header("Cache-Control: no-cache");
header("Content-Type: application/json; charset=UTF-8");
echo json_encode([
  "message" => "Hello, PHP (JSON)",
  "date"    => date('c'),
  "ip"      => $_SERVER['REMOTE_ADDR'] ?? 'unknown'
], JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE);
