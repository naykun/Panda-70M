rank=$NODE_RANK
echo "META FILE /f_ndata/G/dataset/panda/full_shard_64/panda70m_training_full_${rank}.csv"
echo "Saving to /scratch/s3/G/dataset/panda/full_shard_64/part-${rank}"
echo "Logging at panda-s3:part-${rank}"
video2dataset --url_list="/f_ndata/G/dataset/panda/full_shard_64/panda70m_training_full_${rank}.csv" \
              --url_col="url" \
              --caption_col="caption" \
              --clip_col="timestamp" \
              --output_folder="/scratch/s3/G/dataset/panda/full_shard_64/part-${rank}" \
              --save_additional_columns="[matching_score]" \
              --config="video2dataset/video2dataset/configs/panda_70M_s3.yaml"\
	      --enable_wandb=True \
	      --wandb_project="panda-s3" \
    	      --wandb_name="part-${rank}"