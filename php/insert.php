<!----  
	Name: Akash Mukherjee
	Dept: BCA
	Roll: 20BCA22
	Code: Insert Data
---->
<?php 
include'db.php'; 

?>	

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Login</title>
</head>
<body>
	<div class="center">
		<form method="POST" action="">
			<div class="txt_field">
				<input type="text" name="user_name" phlaceholder="Username"><br>
				<input type="text" name="user_password" placeholder="Password"><br>
				<button name="login">Submit</button>
			</div>
		</form>
	</div>
	<?php 
		if (isset($_POST['login'])) {
			// code...
			$user_name= $_POST['user_name'];			#store input name in a veriable
			$user_password= $_POST['user_password'];	#store input password in a veriable
			if (empty($user_name) || empty($user_password)) {	#Check The Fields are empty or not
				// code...
				echo "Enter Username and Password!!";
			}
			else{
				
				// code...
				$sql="INSERT INTO `bca`(`user_name`, `user_password`) VALUES ('$user_name','$user_password')"; #SQL command
				$insert= mysqli_query($connection,$sql);	#run query to save it
			
		}	
		}
		


	?>
</body>
</html>