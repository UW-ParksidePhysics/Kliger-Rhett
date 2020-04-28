
%Cut c of at 1000
c = 1
n = 1000
filename = fopen('Pythagorean_triples.txt', 'wt'); % wt, w means to open files for writing, t means to open it in text mode.
for a = 1:n-2
    for b = a:n-1
        c = sqrt(a^2 + b^2);
        if c == floor(c) & c < n
            fprintf(filename, '%i %i %i\n' , a, b, c); % The %i formats integers, \n creates new line.
        end
    end
end
fclose(filename); 