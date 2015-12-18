<?php
	// [{"info" : "0"}]
	$led1=file_get_contents('teks.txt', true); // membaca data dari file teks
	$led2=file_get_contents('teks2.txt', true); // membaca data dari file teks
	$led3=file_get_contents('teks3.txt', true); // membaca data dari file teks
	
	//$info="0";
	$v = '[';
	$v .= '{"LED" : "1", "INFO": "'.$led1.'"},{"LED" : "2", "INFO": "'.$led2.'"},{"LED" : "3", "INFO": "'.$led3.'"}';
	$v .= ']';
	echo $v;
?>
