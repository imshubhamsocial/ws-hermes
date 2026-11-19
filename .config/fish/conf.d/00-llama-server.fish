# Automatically ensure llama-server is running when entering ws-hermes
if test "$CONTAINER_ID" = "ws-hermes"
    if not systemctl --user is-active --quiet llama-server.service
        systemctl --user start llama-server.service >/dev/null 2>&1 &
    end
end
