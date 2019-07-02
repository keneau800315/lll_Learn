<?php 
	$dsn = "mysql:host=localhost;port=3306;dbname=books;charset=utf8";
	$user = "root";
	$password = "mysql";
	//https://www.php.net/manual/en/pdo.constants.php
    //PDO::ATTR_CASE => PDO::CASE_NATURAL 保持原來字的大小
    //PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION 抓取錯誤訊息
	$options = array( PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_CASE => PDO::CASE_NATURAL);
    //new 一個PDO物件讓我們可以跟資料庫做連結
	$pdo = new PDO($dsn, $user, $password, $options);
?>