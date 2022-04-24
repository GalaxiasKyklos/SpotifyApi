# We need pyenv and virtualenv to manage the python version
brew list pyenv || brew install pyenv
brew list pyenv-virtualenv || brew install pyenv-virtualenv

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
