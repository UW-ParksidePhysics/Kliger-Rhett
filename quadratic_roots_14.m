%Quadratic Example-Rhett Kliger
% takes input from the command line and returns the roots of the quadratic equation 
a = input("Enter the first root of your quadratic: ")
b = input("Enter the second root of your quadratic: ")
c = input("Enter the third root of your quadratic: ")

discriminant = b*b -4*a*c;
[x, x2] = quadratic_roots(a, b, c); % calls fro quadratic_roots

if discriminant < 0
   disp([num2str(x) ' ' , num2str(x2) ' ' , ' Warning:discriminant is negative, roots are imaginary ']);
elseif discriminant == 0
   disp([num2str(x) ' ' , num2str(x2) ' ' , ' Discriminant is zero, roots are repeated '])
else
   disp([num2str(x) ' ' , num2str(x2) ' ' , ' Roots are real ']) 
end


