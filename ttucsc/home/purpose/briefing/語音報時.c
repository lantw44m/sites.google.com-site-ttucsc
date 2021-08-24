#include<stdio.h>
#include<stdlib.h>

int main()
{
	FILE *vbs,*output;
	char s[6];
	char time[5];
	
	//fopen為開檔 打開2.vbs檔案 若檔案不存在則建立該檔案
	//w+為使該檔案可讀可寫
	//詳細請見:http://www.cplusplus.com/reference/clibrary/cstdio/fopen/
	vbs = fopen( "2.vbs" , "w+");

	//以windows系統指令 attrib 更改 2.vbs 檔案為隱藏屬性
	//詳細請由cmd 打上 "attrib /?"
	system("attrib +h 2.vbs");

	//將VBScript呼叫語音功能所需字串寫入檔案內
	//fprintf 如printf使用方式 只是增加第一個參數告知檔案
	fprintf( vbs , "%s" , "CreateObject(\"SAPI.SpVoice\").Speak \"");
	
	//以系統呼叫 time /t 將結果存入1.txt檔案內
	system("time /t > 1.txt");
	
	//開啟1.txt 讀取所得時間
	output = fopen( "1.txt" , "r");
	system("attrib +h 1.txt");
	
	//讀入 上/下午 及時間點到變數
	fscanf( output , "%s" , s);
	fscanf( output , "%s" , time);
	
	//關閉檔案 以利進行system指令將其刪除
	fclose(output);
	system("attrib -h 1.txt");
	system("del 1.txt");
	
	//上下午判斷 可自己將中文字放到變數內測試即可知道數值
	//判斷得知後將要電腦念出的英文字寫到vbs檔案內
	if( s[1] == 87){
		fprintf( vbs , "%s" , "Morning ");
		}	
	if( s[1] == 85){
		fprintf( vbs , "%s" , "Afternoon ");
		}
	
	//將時間寫入檔案 並補上最後的"
	fprintf( vbs , "%s" , time);
	fprintf( vbs , "%c" , '"');

	//關閉檔案 執行唸出 最後刪除該vbs檔
	fclose(vbs);
	system("2.vbs");
	system("attrib -h 2.vbs");
	system("del 2.vbs");
	
	}
