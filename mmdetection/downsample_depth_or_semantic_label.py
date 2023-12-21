downsample = 16
se = box_2d_mask_aug[4]
H, W = se.shape
se_down = se.view(H // downsample, downsample,
            W // downsample, downsample, 1)
se_down = se_down.permute(0, 2, 4, 1, 3).contiguous()
se_down = se_down.view(-1, downsample*downsample)
se_down = torch.max(se_down, dim=-1).values
se_down = se_down.view(H // downsample, W // downsample)
