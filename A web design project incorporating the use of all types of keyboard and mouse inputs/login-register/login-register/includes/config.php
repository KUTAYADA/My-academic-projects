<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

session_start();

require_once 'functions.php';

$base_url = "http://localhost/login-register/";
$page_title = "";
$form_type = "";

$host = "localhost"; $user = "root"; $database = "login_register"; $pass = "admin";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$database", $user, $pass);
} catch(PDOException $e) {
    echo "Check your connection.";
}