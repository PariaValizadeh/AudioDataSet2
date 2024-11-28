# Base image with CUDA and Ubuntu
ARG VARIANT="ubuntu22.04" 
ARG CUDA_VERSION="11.7.1"
FROM nvidia/cuda:${CUDA_VERSION}-devel-${VARIANT}

# User configuration
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set non-interactive mode for APT installations
ARG DEBIAN_FRONTEND=noninteractive

# Install essential development dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    python3-pip \
    git \
    curl \
    bash-completion \
    ssh \
    vim \
    tmux \
    htop \
    ffmpeg

# Copy tmux configuration if needed
COPY config/.tmux.conf /home/$USERNAME/.tmux.conf

# Switch to the created user
USER $USERNAME

# Install Poetry (for Python dependency management)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/home/$USERNAME/.local/bin:$PATH"

# Install additional system dependencies for audio
RUN sudo apt-get update && sudo apt-get install -y \
    pulseaudio \
    alsa-utils \
    libasound2-dev \
    portaudio19-dev \
    && sudo rm -rf /var/lib/apt/lists/*

# Set DEBIAN_FRONTEND back to default
ARG DEBIAN_FRONTEND=dialog

# Set the default user to the non-root user
USER $USERNAME
