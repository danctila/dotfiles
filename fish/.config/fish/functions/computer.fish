function computer
    argparse c/continue f/follow-up -- $argv
    or return

    set base_prompt "Answer in concise Markdown. Put commands in fenced bash code blocks. Do not add extra fluff."
    set prompt (string join " " $argv)

    # Included model on paid Copilot plans. On Copilot Free, chat still counts against the free monthly request quota.
    set model gpt-4.1

    if set -q _flag_continue
        gh copilot -- --model $model --continue
        return
    end

    if set -q _flag_follow_up
        if test -z "$prompt"
            gh copilot -- --model $model --continue
        else
            gh copilot -- --model $model --continue -p "$prompt" \
            2>/dev/null \
            | glow --style dark --width 100
        end
        return
    end

    gh copilot -- --model $model -p "$base_prompt $prompt" \
    2>/dev/null \
    | glow --style dark --width 100
end
