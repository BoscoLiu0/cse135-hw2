<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=UTF-8");
$raw = file_get_contents('php://input');
?><!doctype html><html><head><title>POST Echo (PHP)</title></head><body>
<h1>POST Echo</h1><hr/>
<p>Raw body:</p><pre><?= htmlspecialchars($raw) ?></pre>
<table border="1" cellpadding="6" cellspacing="0">
<?php foreach($_POST as $k=>$v): ?>
<tr><td><?= htmlspecialchars($k) ?></td><td><?= htmlspecialchars($v) ?></td></tr>
<?php endforeach; ?>
</table>
</body></html>
