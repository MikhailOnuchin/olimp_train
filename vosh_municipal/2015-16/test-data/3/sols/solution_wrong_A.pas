var
  n, i, k, a, b, tmp: longint;
  s, s1: string;

procedure swap(var a: longint; var b: longint);
var
  t: longint;
begin
  t := a;
  a := b;
  b := t;
end;

begin
  readln(n);
  k := 0;
  for i := 1000 to 9999 do 
  begin
    a := i div 1000 + i mod 1000 div 100;
    b := i mod 100 div 10 + i mod 10;
    if a < b then
      swap(a, b); 
    {str(a, s);
    str(b, s1);
    s += s1;
    str(n, s1);}
    tmp:=a*100 + b;
    if  (n = tmp) and (k = 0) then
      k := i;
  end;
  writeln(k);
end.
