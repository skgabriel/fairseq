#!/usr/bin/env python

import sweep
from sweep import hyperparam


def get_grid(args):
    return [
        #hyperparam("--criterion", "label_smoothed_cross_entropy"),
        hyperparam("--criterion", "latent_var"),
        hyperparam("--latent-category", 10, save_dir_key=lambda val: f"latent{val}"),
        hyperparam("--latent-token", save_dir_key=lambda val: "ltoken"),
        hyperparam("--latent-layer", save_dir_key=lambda val: "llayer"),
        #hyperparam("--latent-out", save_dir_key=lambda val: "lout"),

        hyperparam("--fp16", save_dir_key=lambda val: "fp16"),
        hyperparam("--max-epoch", 50),
        hyperparam("--arch", "transformer_vaswani_wmt_en_de_big", save_dir_key=lambda val: val),
        hyperparam("--share-all-embeddings", save_dir_key=lambda val: "shareemb"),
        hyperparam("--optimizer", "adam", save_dir_key=lambda val: val),
        hyperparam("--adam-betas", "(0.9, 0.98)", save_dir_key=lambda val: "beta0.9,0.98"),

        hyperparam("--lr-scheduler", "inverse_sqrt"),
        hyperparam("--warmup-init-lr", 1e-7, save_dir_key=lambda val: f"initlr{val}"),
        hyperparam("--warmup-updates", 4000, save_dir_key=lambda val: f"warmup{val}"),
        hyperparam("--lr", 10e-4, save_dir_key=lambda val: f"lr{val}"),
        hyperparam("--min-lr", 1e-9),
        #hyperparam("--lr-scheduler", "fixed"),
        #hyperparam("--lr", 1e-4, save_dir_key=lambda val: f"lr{val}"),

        hyperparam("--clip-norm", 0.0, save_dir_key=lambda val: f"clip{val}"),
        hyperparam("--dropout", 0.3, save_dir_key=lambda val: f"drop{val}"),
        hyperparam("--weight-decay", 0.0, save_dir_key=lambda val: f"wd{val}"),

        #hyperparam("--label-smoothing", 0.1, save_dir_key=lambda val: f"ls{val}"),
        hyperparam("--label-smoothing", 0.0, save_dir_key=lambda val: f"ls{val}"),

        #hyperparam("--update-freq", 4, save_dir_key=lambda val: f"updatefreq{val}"),
        hyperparam("--max-tokens", 3500, save_dir_key=lambda val: f"maxtok{val}"),
        hyperparam("--seed", 2, save_dir_key=lambda val: f"seed{val}"),
        hyperparam("--log-format", "simple"),
        hyperparam("--log-interval", 10),
    ]


def postprocess_hyperparams(args, config):
    """Postprocess a given hyperparameter configuration."""
    # if config['--seq-beam'].current_value <= 8:
    #    config['--max-tokens'].current_value = 400
    # else:
    #    config['--max-tokens'].current_value = 300
    pass


if __name__ == "__main__":
    sweep.main(get_grid, postprocess_hyperparams)
