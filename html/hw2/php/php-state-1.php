<?php
header("Cache-Control: no-cache");
header("Content-Type: text/html; charset=UTF-8");

session_name('CGISESSID');
session_set_cookie_params(['path' => '/']);
session_start();

$name = $_SESSION['username'] ?? ($_POST['username'] ?? '');
if ($name !== '') {
    $_SESSION['username'] = $name;
}
?>
<!doctype html>
<html>
<head><title>PHP Sessions Page 1</title></head>
<body>
  <h1>PHP Sessions Page 1</h1>
  <?php if ($name): ?>
    <p><b>Name:</b> <?= htmlspecialchars($name) ?></p>
  <?php else: ?>
    <p><b>Name:</b> You do not have a name set</p>
  <?php endif; ?>

  <br/><br/>
  <a href="/hw2/php/php-state-2.php">Session Page 2</a><br/>
  <a href="/hw2/php/php-cgiform.html">PHP CGI Form</a><br />
  <form style="margin-top:30px" action="/hw2/php/php-destroy-session.php" method="get">
    <button type="submit">Destroy Session</button>
  </form>
</body>
</html>
