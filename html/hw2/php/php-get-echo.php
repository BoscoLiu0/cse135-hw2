<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=UTF-8");
?><!doctype html><html><head><title>GET Echo (PHP)</title></head><body>
<h1>GET Echo</h1><hr/>
<p>Raw query string: <?= htmlspecialchars($_SERVER['QUERY_STRING'] ?? '') ?></p>
<table border="1" cellpadding="6" cellspacing="0">
<?php foreach($_GET as $k=>$v): ?>
<tr><td><?= htmlspecialchars($k) ?></td><td><?= htmlspecialchars($v) ?></td></tr>
<?php endforeach; ?>
</table>
</body></html>
