# Create a new virtualenv with 3.10.3
pyenv install 3.10.3 -s
pyenv virtualenv 3.10.3 SpotifyApi
pyenv local 3.10.3/envs/SpotifyApi

# Install required packages
pip install -r ./requirements.txt

# Prepare .env file
if [[ ! -e .env ]]; then
  cp .env.template .env
fi
