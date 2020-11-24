<?php
##################################################
# By Manal Shaikh (github.com/ManalShaikh)
# Design credit AdminLite v3(Google up)
# Sorry not sorry for the messy code. 
# Of course I am not responsible for whatever you do with this. Pls dont do anything illegal or bad. Read the license for more info.
# Credits are more than appreciated in any environment.
##################################################
session_start();
/* DATABASE CONFIGURATION */
define('DB_SERVER', 'localhost'); #Localhost recommended
define('DB_USERNAME', 'root'); # Root not recommended incase shit goes wrong.
define('DB_PASSWORD', ''); # XAMPP on dev's PC so leaving it empty. Enter your db's user pw here.
define('DB_DATABASE', 'beatsmonitor');
define("BASE_URL", "http://192.168.0.105/projects/BeatsMonitor/BeatsMonitor/"); // Eg Your website's base URL. Not necessary. Maybe deperecated in future.


function getDB() 
{
	$dbhost=DB_SERVER;
	$dbuser=DB_USERNAME;
	$dbpass=DB_PASSWORD;
	$dbname=DB_DATABASE;
	try {
	$dbConnection = new PDO("mysql:host=$dbhost;dbname=$dbname", $dbuser, $dbpass);	
	$dbConnection->exec("set names utf8");
	$dbConnection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	return $dbConnection;
    }
    catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
	}

}
?>