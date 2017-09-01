<!doctype html>
<html>
  <body>
    <?php
      $filename = rand(1, 1000)."homepage.php";
      $file = fopen("$filename", "w");
      fwrite($file, $_POST["homepagecode"]);
      fclose($file);
      header("Location: ".$filename);
      exit;
      ?>
  </body>
</html>
