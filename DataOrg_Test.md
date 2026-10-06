## The Goal of this set of commands is to download the raw data from the google drive to your local machine, restructure it to the correct project-specific and BIDS formatting, and reupload the data to the derivatives folder for later analyses


# Install Necessary Packages
# pip install gdown 

# Create directory on your local machine to store data
# mkdir raw_dicoms

# Download the data from google drive, paste folder link follwing --folder argument
# python -m gdown --folder  https://drive.google.com/uc?id=FILE-ID  -O ./raw_dicoms
python -m gdown --folder  https://drive.google.com/uc?id=1u1VzCEGK69_SNVC7vCFJsU03pUPBxeXe  -O ./raw_dicoms

# Check that everything looks correct once the download is complete

# Run this next section of code to replace the NiCoE generated ID to the study-specific participant ID 

# Run this next section of code to convert to BIDS formatting

# Navigate through the resulting directory to ensure the correct files are where they should be. You should see data that looks like this:

# Once complete, move on to preprocessing