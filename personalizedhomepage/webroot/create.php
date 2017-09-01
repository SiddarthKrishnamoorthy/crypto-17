<!doctype html>
<html>
  <body>
    <?php
      $file = fopen("homepage.php", "w");
      fwrite($file, $_POST["homepagecode"]);
      fclose($file);
      header("Location: homepage.php");
      exit;
      ?>
  </body>
</html>
