<?php $page = "login"; require_once 'includes/config.php'; require_once 'includes/header.php'; include 'includes/post.php';?>
<style>
    body {
      margin: 0;
      padding: 0;
      background: #f4f4f4;
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .form-kapsayici {
      background: white;
      padding: 40px;
      border-radius: 10px;
      box-shadow: 0 8px 16px rgba(0,0,0,0.1);
      width: 100%;
      max-width: 400px;
    }

    .form-kapsayici h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    input[type="email"], input[type="password"] {
      width: 100%;
      padding: 12px;
      margin: 10px 0 20px 0;
      border: 1px solid #ccc;
      border-radius: 6px;
      box-sizing: border-box;
    }

    button {
      width: 100%;
      background-color: #4CAF50;
      color: white;
      padding: 12px;
      border: none;
      border-radius: 6px;
      font-weight: bold;
      cursor: pointer;
    }

    button:hover {
      background-color: #45a049;
    }

    .link {
      text-align: center;
      margin-top: 15px;
    }

    .link a {
      text-decoration: none;
      color: #4CAF50;
    }

    .error-message {
      background-color:rgba(248, 215, 218, 0.61);
      color: #721c24;
      border: 1px solid #f5c6cb;
      padding: 10px 15px;
      margin: 15px 0;
      border-radius: 5px;
      font-weight: light;
      font-family: Arial, sans-serif;
    }
  </style>
  <div class="form-kapsayici">
    <?php if (isset($_SESSION['error'])): ?>
        <div class="error-message">
            <?= htmlspecialchars($_SESSION['error']) ?>
        </div>
        <?php unset($_SESSION['error']); ?>
    <?php endif; ?>

    <h2>Giriş Yap</h2>
  <form method="POST" action="">
    <input type="hidden" name="form_type" value="login">
    <input type="email" name="email" placeholder="E-posta" required>
    <input type="password" name="password" placeholder="Şifre" required>
    <button type="submit">Giriş Yap</button>
  </form>
    <div class="link">
      <p>Hesabınız yok mu? <a href="kayitol.php">Kayıt Ol</a></p>
    </div>
  </div>
</body>
</html>
