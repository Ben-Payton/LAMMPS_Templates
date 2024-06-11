class LAMMPS_JOB:
    ''' 
    Holds the information necessary to make a lammps job
    '''
    def __init__(self) -> None:
        self.job_name="Unnamed"
        self.units="real"
        pass
    
    def write_submission(self) -> None:
        submission_file_name = self.job_name + ".s"
        file_contents = """
#!/bin/bash

#SBATCH --job-name={JOB_NAME}
#SBATCH --account={ACCOUNT_NUMBER}
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --time=71:59:59
#SBATCH -o stdout
#SBATCH -e stderr
#SBATCH --export=ALL

# Go to the directoy from which our job was launched
cd $SLURM_SUBMIT_DIR

module purge
module load libs/mkl/2021.1
module load mpi/impi/2021.1
module load compilers/intel/2021.1
module load apps/lammps/intel-impi-plumed/23Jun2022
ulimit -s unlimited

echo "running job"


srun lmp -in {IN_FILE_NAME}


echo "job has finished"
""".format(IN_FILE_NAME = self.job_name + ".in",ACCOUNT_NUMBER = 1234,JOB_NAME = self.job_name)
        with open(submission_file_name,"w") as submission_file:
            submission_file.write(file_contents)
        pass



# This section will only run if this script is run directly.
if __name__ == "__main__":

    def main() -> None:
        print("Hello_World")
        test_var = LAMMPS_JOB()
        test_var.write_submission()


    main()