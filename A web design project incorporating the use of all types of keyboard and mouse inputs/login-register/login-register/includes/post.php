<?php 

$form_type = esc($_POST['form_type'] ?? null);

if($form_type == "register") {

    $username = esc($_POST['username']);
    $email = esc($_POST['email']);
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $data = [
        'username' => $username,
        'email' => $email,
        'password' => $password,
    ];

    $table = 'users';

    $register = insert($data, $table);
    header("location:giris.php");

}else if($form_type == "login") {
    
    $email = esc($_POST['email']);
    $password = $_POST['password'];

    $table = 'users';

    $user = get_item( $table, $email);
    $user_pass = $user['password'];

    if ($form_type == "login") {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $user = get_item('users', $email);

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user'] = $user['email'];
        header("location:index.php");
        exit;
    } else {
        $_SESSION['error'] = "Hatalı giriş";
        header('location:giris.php');
        exit;
    }
}

}

?>