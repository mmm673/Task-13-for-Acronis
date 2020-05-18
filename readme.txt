# Task-13-for-Acronis
Для решения данной задачи был получен и проанализирован ассемблерный код:
1) основная часть с выводом сообщения об успешной регистрации:
push    offset String
call    sub_40137E                                       #анализ введенного логина (пункт 2)
push    eax
push    offset byte_40217E
call    sub_4013D8                                       #анализ введенного пароля (пункт 3)
add     esp, 4
pop     eax
cmp     eax, ebx
jz      short loc_40124C
  loc_40124C:
call    sub_40134D                                       #вывод сообщения об успешном вводе логина и пароля (пункт 4)
jmp     short loc_4011E6
WndProc endp

2) анализ введенного логина:
sub_40137E proc near
arg_0= dword ptr  4
mov     esi, [esp+arg_0]
push    esi
  loc_401383:                                             #посимвольная проверка логина
mov     al, [esi]
test    al, al                                            #после проверки логина переходим к подсчету суммы ord от символов (пункт 2.3)
jz      short loc_40139C
cmp     al, 41h                                           #сравнение с "A" - если меньше, то неверный логин (пункт 2.1)
jb      short loc_4013AC
cmp     al, 5Ah                                           #сравнение с "Z" - если не меньше, то уменьшение ord на 32 (пункт 2.2)
jnb     short loc_401394
inc     esi
jmp     short loc_401383
2.1) вывод сообщения об ошибке
  loc_4013AC:
pop     esi
push    30h             ; uType
push    offset aNoLuck  ; "No luck!"
push    offset aNoLuckThereMat ; "No luck there, mate!"
push    dword ptr [ebp+8] ; hWnd
call    MessageBoxA
2.2) уменьшение ord соответствущего символа на 20h, то есть на 32 - изменение регистра
  loc_401394:
call    sub_4013D2
inc     esi
jmp     short loc_401383
2.3) XOR полученной суммы и 5678
  loc_40139C:
pop     esi
call    sub_4013C2                                       #подсчет суммы ord для каждого символа нового логина (пункт 2.4)
xor     edi, 5678h
mov     eax, edi
jmp     short locret_4013C1
2.4) 
  locret_4013C1:
retn
sub_40137E endp
