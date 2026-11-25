# Docker file for VTC based on a pytorch image
FROM debian:trixie-slim

RUN apt-get update && apt-get upgrade -y \
 && apt-get install --no-install-recommends -y ca-certificates git curl ffmpeg git-lfs \
 && git lfs install 

#RUN apt-get update && apt-get upgrade -y \
# && apt-get install --no-install-recommends -y ca-certificates apt-utils git curl ffmpeg git-lfs \
# && git lfs install 

WORKDIR /home/inference

RUN groupadd -g 1000 inference \
 && useradd --group inference -u 1000 -g 1000 inference \
 && chown -R inference /home/inference \
 && chmod -R 744 /home/inference

USER inference

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
#RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/home/inference/.local/bin:$PATH"
RUN git clone --recurse-submodules https://github.com/LAAC-LSCP/VTC.git

WORKDIR /home/inference/VTC

RUN uv sync  --frozen --no-cache

CMD ["uv", "run", "scripts/infer.py", "--wavs", "../inputs", "--output", "../outputs", "--recursive_search", "--device", "cpu"]

#TODO:
# check out uv optimization recommends to remove/externalize cache: see: https://docs.astral.sh/uv/guides/integration/docker/ 
# can I remove CUDA libs and replace with runtime? see https://mveg.es/posts/optimizing-pytorch-docker-images-cut-size-by-60percent/
