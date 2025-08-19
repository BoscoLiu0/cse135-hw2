<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=UTF-8");

session_name('CGISESSID');
session_set_cookie_params(['path' => '/']);
session_start();

$_SESSION = [];
if (ini_get('session.use_cookies')) {
    $params = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000,
        $params['path'], $params['domain'],
        $params['secure'], $params['httponly']
    );
}
session_destroy();
?>
<!doctype html>
<html>
<head><title>PHP Session Destroyed</title></head>
<body>
  <h1>Session Destroyed</h1>
  <a href="/hw2/php/php-cgiform.html">Back to the PHP CGI Form</a><br />
  <a href="/hw2/php/php-state-1.php">Back to Page 1</a><br />
  <a href="/hw2/php/php-state-2.php">Back to Page 2</a>
</body>
</html>
