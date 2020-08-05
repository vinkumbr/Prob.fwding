%% Bounds for pkndelta- lower_approx and upper_approx for the binary
% tree using normal approximation
clear all

p=0.95:0.00001:1;

k=100;
delta=0.1;
H=50;
ckdelta=2*(k-1)-2*log(delta);
denom=2^(H+1)-1;
lower=zeros(1,101);
upper=zeros(1,101);
tau_lower=zeros(1,101);
tau_upper=zeros(1,101);
minp_expr=zeros(1,101);
trans_expr=zeros(1,101);
j=1;
for n=100:1:200
    sum_lower=0;
    sum_upper=0;
    sum_ergodic=0;
    for l=0:1:H-1
        zetap=p.^l;
        a=k/n;
        kldiv=a.*log(a./zetap)+(1-a).*log((1-a)./(1-zetap));
        kldiv(kldiv<0)=0;
        if n==100
            Cnpl_upper=1-zetap.^n;
        else
            Cnpl_upper=normcdf(sign(k/n-zetap).*sqrt(2*n.*kldiv));
        end
        sum_upper=sum_upper+2^(l+1).*Cnpl_upper;
        b=(k-1)/n;
        kldiv2=b.*log(b./zetap)+(1-b).*log((1-b)./(1-zetap));
        Cnpl_lower=normcdf(sign((k-1)/n-zetap).*sqrt(2*n.*kldiv2));
        sum_lower=sum_lower+2^(l+1).*Cnpl_lower;
        sum_ergodic=sum_ergodic+2^(l+1).*binocdf(k-1,n,zetap);
    end
    sum_upper=sum_upper./denom;
    sum_lower=sum_lower./denom;
    sum_ergodic=sum_ergodic./denom;
    lhs_upper=find(sum_upper<=delta);
    lhs_lower=find(sum_lower<=delta);
    actual=find(sum_ergodic<=delta);
    if isempty(lhs_upper)
        upper_index=length(p);
    else
        upper_index=lhs_upper(1);
    end
    lower_index=lhs_lower(1);
    upper(j)=p(upper_index);
    lower(j)=p(lower_index);
    tau_upper(j)=n*((2*upper(j))^(H+1)-1)/((2*upper(j))-1);
    tau_lower(j)=n*((2*lower(j))^(H+1)-1)/((2*lower(j))-1);
     actual_index=actual(1);
     minp_expr(j)=p(actual_index);
     trans_expr(j)=n*((2*minp_expr(j))^(H+1)-1)/((2*minp_expr(j))-1);
    j=j+1
end
%minp_expr=[0.99998  0.9999   0.99978  0.99965  0.99952  0.99938  0.99923  0.99909  0.99894  0.99879  0.99864  0.99849  0.99834  0.99819  0.99804  0.99789  0.99774  0.9976   0.99745  0.9973   0.99715  0.99701  0.99686  0.99672  0.99657  0.99643  0.99629  0.99614  0.996    0.99586  0.99572  0.99558  0.99545  0.99531  0.99517  0.99504  0.9949   0.99477  0.99463  0.9945  0.99437  0.99424  0.99411  0.99398  0.99385  0.99372  0.99359  0.99347  0.99334  0.99321  0.99309  0.99297  0.99284  0.99272  0.9926   0.99248  0.99236  0.99224  0.99212  0.992    0.99188  0.99177  0.99165  0.99154  0.99142  0.99131  0.99119  0.99108  0.99097  0.99085  0.99074  0.99063  0.99052  0.99041  0.9903   0.9902   0.99009  0.98998  0.98987  0.98977  0.98966  0.98956  0.98945  0.98935  0.98925  0.98914  0.98904  0.98894  0.98884  0.98874  0.98864  0.98854  0.98844  0.98834  0.98824  0.98814  0.98804  0.98795  0.98785  0.98776];
%trans_expr=[ 1.12481955e+17   1.13171336e+17   1.13635315e+17   1.14035386e+17   1.14425989e+17   1.14752099e+17   1.15013336e+17   1.15320177e+17   1.15562095e+17   1.15794471e+17   1.16017428e+17   1.16231088e+17   1.16435569e+17   1.16630990e+17   1.16817469e+17   1.16995121e+17   1.17164061e+17   1.17380864e+17   1.17532803e+17   1.17676364e+17   1.17811658e+17   1.17995582e+17   1.18114734e+17   1.18282881e+17   1.18386304e+17   1.18539069e+17   1.18684326e+17   1.18764937e+17   1.18895386e+17   1.19018606e+17   1.19134685e+17   1.19243713e+17   1.19403328e+17   1.19498570e+17   1.19587017e+17   1.19726486e+17   1.19801646e+17   1.19928104e+17   1.19990299e+17   1.20104053e+17   1.20211600e+17   1.20313009e+17   1.20408352e+17   1.20497700e+17   1.20581123e+17   1.20658689e+17   1.20730468e+17   1.20854889e+17   1.20915333e+17   1.20970189e+17   1.21078014e+17   1.21180468e+17   1.21219007e+17   1.21310839e+17   1.21397472e+17   1.21478964e+17   1.21555369e+17   1.21626742e+17   1.21693138e+17   1.21754611e+17   1.21811215e+17   1.21921976e+17   1.21969030e+17   1.22070429e+17   1.22108134e+17   1.22200361e+17   1.22228913e+17   1.22312155e+17   1.22390996e+17   1.22406191e+17   1.22476319e+17   1.22542178e+17   1.22603809e+17   1.22661256e+17   1.22714560e+17   1.22823262e+17   1.22868433e+17   1.22909583e+17   1.22946752e+17   1.23039611e+17   1.23068960e+17   1.23154145e+17   1.23175826e+17   1.23253480e+17   1.23327442e+17   1.23337907e+17   1.23404547e+17   1.23467596e+17   1.23527086e+17   1.23583051e+17   1.23635522e+17   1.23684531e+17   1.23730109e+17   1.23772288e+17   1.23811100e+17   1.23846574e+17   1.23878743e+17   1.23967822e+17   1.23993488e+17   1.24076187e+17];
t1=100:1:200;
figure(1)
plot(t1,minp_expr,t1,lower,'o',t1,upper,'+')
legend('numerically from Eq. (4)', 'lower bound from Eq. (6)','upper bound from Eq. (6)')
xlabel('Number of coded packets (n)')
ylabel('p_{k,n,\delta}')

figure(2)
plot(t1,trans_expr,t1,tau_lower,'o',t1,tau_upper,'+')
legend('numerically from Eq. (4)', 'lower bound from Eq. (6)','upper bound from Eq. (6)')
xlabel('Number of coded packets (n)')
ylabel('\tau_{k,n,\delta}')