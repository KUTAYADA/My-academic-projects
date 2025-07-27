<?php 
function esc($val) {
    return htmlspecialchars($val ?? '', ENT_QUOTES | ENT_HTML5, 'UTF-8');
}

function insert($data, $table) {
    global $pdo;

    $sql = "INSERT INTO $table (username, password, email, created_at) VALUES (:username, :password, :email, :created_at)";
    $stmt = $pdo->prepare($sql);

    $stmt->execute([
        ':username' => $data['username'],
        ':password' => $data['password'], 
        ':email' => $data['email'],
        ':created_at' => date('Y-m-d H:i:s')
    ]);
}

function get_item($table, $uniq) {
    global $pdo;

    $sql = "SELECT * FROM `$table` WHERE email = :email LIMIT 1";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([':email' => $uniq]);
    return $stmt->fetch(PDO::FETCH_ASSOC);
}
