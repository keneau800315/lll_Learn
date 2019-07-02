<?php
//用來記錄錯誤訊息
$errMsg ="";  
try {
	
	//require_once引入檔案，這裡用來建立pdo物件，連線到資料庫
	require_once 'mysqlconnect.php';

	//sql指令
	$sql = "select * from bookstore"; 


	//透過pdo物件將指令傳到DB server去執行，並傳回PDOStatement
	//之後就可以使用PDOStatement的fetch方法來取回一筆資料
	$products = $pdo->query($sql);

} catch (PDOException $e) {//若有發生錯誤
	//將要顯示的訊息準備好
	//呈現給使用者看
	//$errMsg = "系統錯誤，請通知系統維護人員"."<br>";
	//開發測試
	$errMsg = $errMsg . "錯誤 : " . $e -> getMessage() . "<br>";
	$errMsg = $errMsg . "行號 : " . $e -> getLine() . "<br>";
}



?>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>My bookstore</title>
<style >
td {
	border:   1px dotted #2D99E6;
}	


</style>


</head>
<body>



<?php 
if( $errMsg != ""){ //如果錯誤訊息不為空字串，代表有錯，程式應停止執行
	echo "<center>", $errMsg, "</center>"; //顯示錯誤訊息
	exit(); //程式停止執行
}
?>
<!-- &nbsp;表示一個空白 -->
<div style="background-color:#ACBBEB;text-align:right">&nbsp;</div>
<table align="center" >
	<tr bgcolor="#758FDE"><th>書號</th><th>書名</th><th>價格</th><th>作者</th></tr>



<?php
	//fetch_assoc() 以colums_names取值	
	while($prodRow = $products->fetch(PDO::FETCH_ASSOC)){
?>

		<tr >
			<td><?php echo $prodRow["psn"]; ?> </td>
			<td><?php echo $prodRow["pname"];?></td>
			<td><?php echo $prodRow["price"];?></td>
			<td><?php echo $prodRow["author"];?></td>
			
		</tr>
<?php
	}
?>
<!-- div 分開來一塊區域 -->


</table> 
<div style="background-color:#ACBBEB;text-align:right"><a href="home.html" >返回主頁面</a></div><br>    
</body>
</html>