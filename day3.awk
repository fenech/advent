BEGIN { xs=0;ys=0;xr=0;yr=0; FS = "" }
{
    for(i=1;i<=NF;++i) {
        if (i % 2) {
            if($i =="^") ys+=1;
            else if ($i ==">")xs+=1;
            else if ($i == "v") ys-=1;
            else if ($i == "<") xs-=1;
            a[xs,ys]+=1
        }
        else {
            if($i =="^") yr+=1;
            else if ($i ==">")xr+=1;
            else if ($i == "v") yr-=1;
            else if ($i == "<") xr-=1;
            a[xr,yr]+=1
        }
    }
}

END { print length(a)}