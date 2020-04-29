%Take Pythagorean triples and 
% write out the complex and real roots of the quadratic equation solved for the a, b, and c 

fileID = fopen('Pythagorean_triples.txt', 'r'); 
PT = fscanf(fileID, '%d %d %d\n', [3, Inf]); % %d is for integers, \n is to read new line 
fclose(fileID); 
filename = fopen('pythagorean_triple_quadratic_roots.txt', 'wt'); % wt, w means to open files for writing, t means to open it in text mode.

for triple = PT 
    a = triple(1); %a is the first entry in the triple
    b = triple(2); %b is the second entry in the triple
    c = triple(3); %c is the third entry in the triple
    [x, x2] = quadratic_roots(a, b, c);
    disp([num2str(triple.'), ' ',num2str(x), ' ', num2str(x2)])
    fprintf(filename, '%i %i %i %g%+gi %g%+gi\n' , a, b, c, real(x),imag(x), real(x2), imag(x2)); % The %i formats integers, \n creates new line.
end 
fclose(filename);

%SUCCESS% 