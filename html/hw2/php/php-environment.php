<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=UTF-8");
?><!doctype html><html><head><title>PHP Environment</title></head><body>
<h1>Environment Variables</h1><hr/>
<pre><?php
ksort($_SERVER); print_r($_SERVER);
?></pre>
</body></html>
