rank=$NODE_RANK
echo "META FILE /f_ndata/G/dataset/panda/full_shard/panda70m_training_full_${rank+1}.csv"
echo "Saving to /f_ndata/G/dataset/panda/full_shard/part-${rank}"
echo "Logging at panda/part${rank}"
video2dataset --url_list="/f_ndata/G/dataset/panda/full_shard/panda70m_training_full_${rank+1}.csv" \
              --url_col="url" \
              --caption_col="caption" \
              --clip_col="timestamp" \
              --output_folder="/f_ndata/G/dataset/panda/full_shard/part-${rank}" \
              --save_additional_columns="[matching_score]" \
              --config="video2dataset/video2dataset/configs/panda_70M.yaml"\
	      --enable_wandb=True \
	      --wandb_project="panda" \
    	      --wandb_name="part${rank}"