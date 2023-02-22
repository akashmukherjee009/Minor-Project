

<?php 
	include'db.php';
	session_start();
	$user_name= $_POST['user_name'];
	$user_password= $_POST['user_password'];
	$_SESSION['user_name']= $user_name;
	$_SESSION['user_password']=$user_password;
	$sql= "SELECT * FROM `bca` WHERE `bca`.`user_name`='$user_name'";
	$login= mysqli_query($connection,$sql);
	while ($row= mysqli_fetch_assoc($login)) {
		// code...
		$db_user_name= $row['user_name'];
		$db_user_password= $row['user_password'];
		if(($user_password==$db_user_password) && ($db_user_name==$user_name)) {
			// code...
			echo "Hello";
		}
		else{
			echo "Wrong password";
		}
	}



?>
