conda activate ratethepauper
conda env export | grep -v "^prefix: " > environment.yml
