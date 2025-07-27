<?php 

$is_auth = false;
if(isset($_SESSION['user'])) {
    $user = get_item('users', $_SESSION['user']);
    $email = $user['email'];
    $username = $user['username'];

    $is_auth = true;
}else {
    $is_auth = false;
}


if(isset($page)) {
    if($page == "homepage") {
        $page_title = "Kutay Ada Öz";
        
    }else if($page == "login") {
        $page_title = "Giriş Yap";
    }else if($page == "register") {
        $page_title = "Kayıt Ol";
    }
}


?>

<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title><?= $page_title ?></title>
</head>
<body>